#!/usr/bin/python3
"""lock boxes interview question"""

from collections import deque


def canUnlockAll(boxes):
    """
    using the breadth-first search (BFS) algorithm
    to solve the lockboxes
    """
    n = len(boxes)
    unlocked = [False]*n
    unlocked[0] = True
    q = deque([0])

    while q:
        box = q.popleft()
        for key in boxes[box]:
            if not unlocked[key]:
                unlocked[key] = True
                q.append(key)

    return all(unlocked)
