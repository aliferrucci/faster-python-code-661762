"""Calculate grades - bisect example"""

cutoffs = [60, 70, 80, 90]
names = 'FDCBA'


def grade(score):
    """Give a letter grade from numeric score

    >>> grade(80)
    'C'
    """
    for cutoff, name in zip(cutoffs, names):
        if score < cutoff:
            return name
    return 'A'


def test_grades():
    cases = [
        (100, 'A'),
        (92, 'A'),
        (87, 'B'),
        (76, 'C'),
        (62, 'D'),
        (60, 'D'),
        (0, 'F'),
    ]

    for score, expected in cases:
        assert grade(score) == expected


# Run in ipython with:
# %run grades.py
# %timeit grade(74)
# and with the optimized version: timeit grade2(74)
if __name__ == '__main__':
    test_grades()
