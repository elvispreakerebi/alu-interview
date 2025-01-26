#!/usr/bin/python3
"""
Module to calculate how much water will be retained after it rains.
"""


def rain(walls):
    """
    Calculate how many square units of water will be retained after it rains.
    Args:
        walls: list of non-negative integers representing wall heights
    Returns:
        Integer indicating total amount of rainwater retained
    """
    if not walls:
        return 0

    n = len(walls)
    water = 0

    # For each element, find the maximum level of water it can trap
    for i in range(1, n - 1):
        # Find maximum element on its left
        left_max = max(walls[:i])
        
        # Find maximum element on its right
        right_max = max(walls[i + 1:])
        
        # The amount of water that can be stored at current position
        min_height = min(left_max, right_max)
        if min_height > walls[i]:
            water += min_height - walls[i]

    return water