#!/usr/bin/python3
"""
Task 0 - minimum operations
"""


def minOperations(n):
    """
    Calculates the least number of operations needed to give an exact result
    """
    if not isinstance(n, int):
        return 0
    op_cnt = 0
    clip_b = 0
    done = 1
    while done < n:
        if clip_b == 0:
            clip_b = done
            done += clip_b
            op_cnt += 2
        elif n - done > 0 and (n - done) % done == 0:
            clip_b = done
            done += clip_b
            op_cnt += 2
        elif clip_b > 0:
            done += clip_b
            op_cnt += 1
    return op_cnt

