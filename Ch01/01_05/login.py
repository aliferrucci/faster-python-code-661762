"""Example login code"""
from crypt import crypt
import sqlite3

salt = '$6$ZmBkxkRFj03LQOvr'  # Bad security, store safely
db = sqlite3.connect('passwords.db')
db.row_factory = sqlite3.Row  # Access columns by names


def user_passwd(user):
    """Get user password from db"""
    cur = db.cursor()
    cur.execute('SELECT passwd FROM users WHERE user = ?', (user, ))
    row = cur.fetchone()
    if row is None:  # No such user
        raise KeyError(user)
    return row['passwd']


def encrypt_passwd(passwd):
    """Encrypt user password"""
    return crypt(passwd, salt)


# Test results of decorator using in terminal:
# kernprof -l prof.py
# to view results: python -m line_profiler prof.py.lprof
# In ipython (must remove @profile decorator):
# %run -n prof.py and then cases = list(gen_cases(1000))
# %load_ext line_profiler
# %lprun -f login bench_login(cases)
# @profile
def login(user, password):
    """Return True is user/password pair matches"""
    try:
        db_passwd = user_passwd(user)
    except KeyError:
        return False

    passwd = encrypt_passwd(password)
    return passwd == db_passwd
