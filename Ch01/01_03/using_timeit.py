"""Using "timeit"""
from timeit import timeit

items = {
    'a': 1,
    'b': 2,
}
default = -1


def use_catch(key):
    """Use try/catch to get a key with default"""
    try:
        return items[key]
    except KeyError:
        return default


def use_get(key):
    """Use dict.get to get a key with default"""
    return items.get(key, default)


if __name__ == '__main__':
    # Key is in the dictionary
    print('catch', timeit('use_catch("a")', 'from __main__ import use_catch'))
    print('get', timeit('use_get("a")', 'from __main__ import use_get'))

    # Key is missing from the dictionary
    print('catch', timeit('use_catch("x")', 'from __main__ import use_catch'))
    print('get', timeit('use_get("x")', 'from __main__ import use_get'))

# Can test in ipython:
# In ipython (in terminal), use %run -n using_timeit.py
# the -n tells the command line not to load the main function
# only the functions
# then %timeit use_get('a')
