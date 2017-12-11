import requests
import os
import sys


class upload_in_chunks(object):
    def __init__(self, filename, chunksize=1 << 13):
        self.filename = filename
        self.chunksize = chunksize
        self.totalsize = os.path.getsize(filename)
        self.readsofar = 0

    def __iter__(self):
        with open(self.filename, 'rb') as file:
            while True:
                data = file.read(self.chunksize)
                if not data:
                    sys.stdout.write("\n")
                    break
                self.readsofar += len(data)
                percent = self.readsofar * 1e2 / self.totalsize
                sys.stdout.write("\r{percent:3.0f}%".format(percent=percent))
                yield data

    def __len__(self):
        return self.totalsize


class IterableToFileAdapter(object):
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.length = len(iterable)

    def read(self, size=-1):  # TBD: add buffer for `len(data) > size` case
        return next(self.iterator, b'')

    def __len__(self):
        return self.length


def remove_file(file):
    try:
        os.remove(file)
    except Exception as e:
        pass


def download(url, account, password, admin=None, path="/tmp/"):
    url = 'https://%s:7071/home/%s/?fmt=tgz' % (url, account)
    path = path + account + '.tgz'
    remove_file(path)
    if admin is not None:
        auth_user = admin
    else:
        auth_user = account
    try:
        response = requests.get(url, stream=True, auth=(auth_user, password))
        response.raise_for_status()
        print "Starting download of account %s" % (account)
        bytes = 0
        with open(path, 'wb') as handle:
            for block in response.iter_content(1024):
                handle.write(block)
                bytes += 1024
                sys.stdout.write("\r" + str(bytes) + " bytes")
        print "\nDownload %s finished" % (account)
        return "success"
    except Exception as e:
        return "failed: %s" % (e)


def upload(url, account, password, admin=None, path="/tmp/"):
    url = 'https://%s:7071/home/%s/?fmt=tgz' % (url, account)
    path = path + account + '.tgz'
    if admin is not None:
        auth_user = admin
    else:
        auth_user = account
    try:
        print "Starting upload of account %s" % (account)
        it = upload_in_chunks(path, 10)
        response = requests.post(url, data=IterableToFileAdapter(it))
        print "Upload %s finished" % (account)
        return ("success")
    except Exception as e:
        return "failed: %s" % (e)


def migrate(host1, host2,
            user1, user2,
            password1, password2,
            authuser1=None, authuser2=None,
            path1="/tmp/", path2="/tmp/"):
    mig = download(host1, user1, password1, admin=authuser1, path=path1)
    print mig
    if (mig == "success"):
        if (user1 != user2):
            remove_file(path2 + user2 + '.tgz')
            os.symlink(path1 + user1 + '.tgz', path2 + user2 + '.tgz')
        mig = upload(host2, user2, password2, admin=authuser2, path=path2)
        print mig
        if (mig == "success"):
            return "Account successfully migrated"
        else:
            return "upload error"
    else:
        return "download error"
