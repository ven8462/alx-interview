#!/usr/bin/python3
"""lock boxes interview question"""

from collections import deque


def canUnlockAll(boxes):
    """
    using the breadth-first search (BFS) algorithm
    to solve the lockboxes
    """

    if boxes is None or boxes == []:
        return False

    num_box = len(boxes)
    keys = [0]  # Start with the first box unlocked

    for w in keys:
        for z in boxes[w]:
            if z not in keys and z < num_box:
                keys.append(z)

    if len(keys) != num_box:  # Check if all boxes can be opened
        return False
    return True
