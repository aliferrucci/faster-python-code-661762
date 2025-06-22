"""Encrypt password with sha256 - checking another option"""

from login import salt

from hashlib import sha256

salt256 = salt.encode('utf-8')  # Convert to bytes


# Running this code instead of manual generation
# ipython: %run login.py
# passwd = 'duck season'
# %run enc256.py
# encrypt_passwd2(passwd)
# compare both functions:
# %timeit encrypt_passwd(passwd)
# %timeit encrypt_passwd2(passwd)
def encrypt_passwd2(passwd):
    """Encrypt password with sha256"""
    return sha256(passwd.encode('utf-8') + salt256).hexdigest()
