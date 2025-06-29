"""Close driver example - using KDTree"""

import math
from random import random


def distance(loc1, loc2):
    x1, y1 = loc1
    x2, y2 = loc2

    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


def find_closest(loc, drivers):
    """Find closest driver using min"""
    def dist(driver):
        return distance(driver, loc)

    return min(drivers, key=dist)


def gen_drivers(lat, lng, count=1000):
    """Generate list of drivers"""
    # 1 degree is ~ 69miles/110km
    return [(lat + random(), lng + random()) for _ in range(1000)]


def test_find_closest():
    lat, lng = 34.3852712, -119.487444  # lynda office

    drivers = gen_drivers(lat, lng)
    closest = find_closest((lat, lng), drivers)

    assert closest in drivers

    loc = (lat, lng)
    min_dist = distance(loc, closest)

    for driver in drivers:
        if driver == closest:
            continue
        assert distance(driver, loc) >= min_dist


# Test in ipython
# %run drivers.py
# lat, lng = 34.3852712, -119.487444
# drivers = gen_drivers(lat, lng)
# %timeit find_closest((lat, lng), drivers)
# profile it: %prun find_closest((lat, lng), drivers)
if __name__ == '__main__':
    test_find_closest()
