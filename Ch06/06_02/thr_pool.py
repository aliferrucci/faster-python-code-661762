"""Thread Pool Example"""

from collections import namedtuple
from datetime import datetime
from urllib.request import urlopen
import json

User = namedtuple('User', 'login name joined')


def user_info(login):
    """Get user information from github"""
    fp = urlopen('https://api.github.com/users/{}'.format(login))
    reply = json.load(fp)

    joined = datetime.strptime(reply['created_at'], '%Y-%m-%dT%H:%M:%SZ')
    return User(login, reply['name'], joined)


def users_info(logins):
    """Get user information for several users"""
    return [user_info(login) for login in logins]


# In ipython:
# %run thr_pool
# %time users_info(logins)
# Shows CPU < wall time which means waiting a lot for I/O
if __name__ == '__main__':
    logins = [
        'gvanrossum',
        'wesm',
        'tebeka',
        'torvalds',
    ]
