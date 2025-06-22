"""memory_profiler example"""


# Add the memory_profiler decorator
# Terminal: python -m memory_profiler sos.py
# Shows memory usage on line 9
# If use mprof:
# remove decorator and change line 22 to 100,000,000
# and run: mprof run sos.py in terminal and view file
# with mprof plot name_of_file.dat
# show memory usage over time
@profile
def sum_of_diffs(vals):
    """Compute sum of diffs"""
    vals2 = vals[1:]

    total = 0
    for v1, v2 in zip(vals, vals2):
        total += v2 - v1

    return total


if __name__ == '__main__':
    vals = list(range(1, 1_000_000, 3))
    print(sum_of_diffs(vals))
