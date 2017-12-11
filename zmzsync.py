#!/usr/bin/env python
import argparse
from argparse import RawTextHelpFormatter
from migration import migrate
parser = argparse.ArgumentParser(
    description='Migrate an zimbra account content to another',
    formatter_class=RawTextHelpFormatter)
parser.add_argument('--host1', action='store', dest='host1',
                    help='Source zimbra server', required=True)
parser.add_argument('--host2', action='store', dest='host2',
                    help='Destination zimbra server', required=True)
parser.add_argument('--user1', action='store', dest='user1',
                    help='User to login on host1', required=True)
parser.add_argument('--user2', action='store', dest='user2',
                    help='User to login on host2', required=True)
parser.add_argument('--password1', action='store', dest='password1',
                    help='Password for user1', required=True)
parser.add_argument('--password2', action='store', dest='password2',
                    help='Password for user2', required=True)
parser.add_argument('--authuser1', action='store', dest='authuser1',
                    help='User to auth with on host1', default=None)
parser.add_argument('--authuser2', action='store', dest='authuser2',
                    help='User to auth with on host2', default=None)

argslist = parser.parse_args()

print migrate(
    argslist.host1,
    argslist.host2,
    argslist.user1,
    argslist.user2,
    argslist.password1,
    argslist.password2,
    argslist.authuser1,
    argslist.authuser2
)
