FROM python:2.7

RUN mkdir -p /opt/zmzsync

ADD __init__.py /opt/zmzsync

ADD migration.py /opt/zmzsync

ADD requirements.txt /opt/zmzsync

ADD zmzsync.py /opt/zmzsync

RUN pip install -r /opt/zmzsync/requirements.txt

RUN ln -s /opt/zmzsync/zmzsync.py /usr/bin/zmzsync

CMD ["/usr/bin/zmzsync"]

