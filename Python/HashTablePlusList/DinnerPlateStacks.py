# Definition for a binary tree node.
import heapq
import unittest

# Read about enumerate in python
from collections import defaultdict
from typing import List


class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.pq = []
        self.stacks = []
        return

    def push(self, val: int) -> None:
        if not self.pq:
            self.stacks.append([val])
            heapq.heappush(self.pq, len(self.stacks)-1)
        else:
            index = heapq.heappop(self.pq)
            self.stacks[index].append(val)
            if len(self.stacks[index]) == 1:
                heapq.heappush(self.pq, index)
        return

    def pop(self) -> int:
        resultIndex = len(self.stacks) - 1
        while resultIndex >= 0 and len(self.stacks[resultIndex]) == 0:
            resultIndex -= 1

        result = self.popAtStack(resultIndex)
        return result

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks):
            return -1

        if len(self.stacks[index]) > 0:
            result = self.stacks[index].pop()
            if len(self.stacks[index]) <= 1:
                heapq.heappush(self.pq, index)
            return result

        return -1

class DinnerPlateStacks(unittest.TestCase):

    def test_Leetcode(self):
        print([1])

if __name__ == '__main__':
    unittest.main()