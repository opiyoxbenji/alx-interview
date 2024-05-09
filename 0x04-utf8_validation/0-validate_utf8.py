#!/usr/bin/python3
"""
Define validUTF8(data) function that validates whether a
string of ints represents a valid UTF-8 encoding.
"""
from itertools import takewhile


def int_to_bits(nums):
    """
    Helper function to convert ints to bits
    """
    for num in nums:
        bits = []
        mask = 1 << 8
        while mask:
            mask >>= 1
            bits.append(bool(num & mask))
        yield bits


def validUTF8(data):
    """
    Validates if a list of ints represents a valid UTF-8 encoding
    Args:
        data: List of ints representing possible UTF-8 encoding
    Return:
        bool: True if the list is a valid UTF-8 encoding, False otherwise
    """
    bits = int_to_bits(data)
    for byte in bits:
        if byte[0] == 0:
            continue
        ones = sum(takewhile(bool, byte))
        if ones <= 1:
            return False
        if ones >= 4:
            return False

        for _ in range(ones - 1):
            try:
                byte = next(bits)
            except StopIteration:
                return False
            if byte[0:2] != [1, 0]:
                return False
    return True
