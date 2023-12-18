#!/usr/bin/env python3

# Author ID: cfederici

set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set2 = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14}

match = (set1 | set2)
join = (set1 & set2)
diff = (set1.symmetric_difference(set2))

def join_sets(set1, set2):
    # join_sets will return a set that contains every value from both s1 and s2
    return set1 | set2
def match_sets(set1, set2):
    # match_sets will return a set that contains all values found in both s1 and s2
    return set1 & set2
def diff_sets(set1, set2):
    # diff_sets will return a set that contains all different values which are not shared between the sets
    return set1.symmetric_difference(set2)
if __name__ == '__main__':
    set1 = set(range(1,10))
    set2 = set(range(5,15))
    print('set1: ', set1)
    print('set2: ', set2)
    print('join: ', join_sets(set1, set2))
    print('match: ', match_sets(set1, set2))
    print('diff: ', diff_sets(set1, set2))
