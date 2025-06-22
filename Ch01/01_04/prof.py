"""Example using cProfile"""
from login import login
from random import random


def gen_cases(n):
    """Generate tests cases"""
    for i in range(n):
        if random() > 0.1:  # 90% of logins are OK
            yield ('daffy', 'rabbit season')
        else:
            if random() < 0.2:
                yield ('tweety', 'puddy tat')  # no such user
            else:
                yield ('daffy', 'duck season')


def bench_login(cases):
    """Benchmark login with test cases"""
    for user, passwd in cases:
        login(user, passwd)


if __name__ == '__main__':
    n = 1000
    cases = list(gen_cases(n))

    # Test using command: python -m cProfile prof.py
    # Shows profile of whole file including setupcode and testcases
    if 0:
        bench_login(cases)

    # Test using command: python prof.py
    # Target code we want to profile
    if 0:
        import cProfile
        cProfile.run('bench_login(cases)')

    # Test using command: python prof.py
    # Generate output file using pstats to drill it
    # python -m pstats prof.out
    # stats 10 or sort cumtime (sort culminated time) then stats 10
    # Change UI using SnakeViz
    # In command line: snakeviz prof.out
    # In ipython: %run -n prof.py
    # cases = list(gen_cases(1000))
    # %prun bench_login(cases) sort by time
    # %prun? help method
    # %prun -s cumulative bench_login(cases) sort by cumulative time
    if 1:
        import cProfile
        cProfile.run('bench_login(cases)', filename='prof.out')
