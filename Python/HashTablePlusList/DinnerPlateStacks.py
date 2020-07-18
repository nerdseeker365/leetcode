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
        if self.capacity <= 0:
            return

        if not self.pq:
            self.stacks.append([val])
            if self.capacity > 1:
                heapq.heappush(self.pq, len(self.stacks)-1)
        else:
            index = heapq.heappop(self.pq)
            while len(self.stacks[index]) == self.capacity and self.pq:
                index = heapq.heappop(self.pq)

            if len(self.stacks[index]) < self.capacity:
                self.stacks[index].append(val)
                if len(self.stacks[index]) < self.capacity:
                    heapq.heappush(self.pq, index)
            else:
                self.stacks.append([val])
                if self.capacity > 1:
                    heapq.heappush(self.pq, len(self.stacks) - 1)
        return

    def pop(self) -> int:

        resultIndex = len(self.stacks) - 1
        while resultIndex >= 0 and len(self.stacks[resultIndex]) == 0:
            resultIndex -= 1

        result = self.popAtStack(resultIndex)
        return result

    def popAtStack(self, index: int) -> int:
        if self.capacity <= 0:
            return -1

        if index >= len(self.stacks):
            return -1

        if len(self.stacks[index]) > 0:
            result = self.stacks[index].pop()
            if len(self.stacks[index]) < self.capacity:
                heapq.heappush(self.pq, index)
            return result

        return -1

class DinnerPlateStacks(unittest.TestCase):

    def test_WrongAnswer(self):
        # ["DinnerPlates", "push", "push", "push", "popAtStack", "pop", "pop"]
        # [[1], [1], [2], [3], [1], [], []]
        # expected: [null,null,null,null,3,2,1]
        # output:   [null,null,null,null,2,3,1]
        dinnerPlates = DinnerPlates(1)
        dinnerPlates.push(1)
        dinnerPlates.push(2)
        dinnerPlates.push(3)
        self.assertEqual(2, dinnerPlates.popAtStack(1))
        self.assertEqual(3, dinnerPlates.pop())
        self.assertEqual(1, dinnerPlates.pop())
        return

    def test_WrongAnswer2(self):
        # ["DinnerPlates", "push", "push", "push", "push", "push", "push", "push", "push", "popAtStack", "popAtStack",
        # "popAtStack", "popAtStack", "push", "push", "push", "push", "push", "push", "push", "push", "pop", "pop",
        # "pop", "pop"]
        # [[2], [471], [177], [1], [29], [333], [154], [130], [333], [1], [0], [2], [0], [165], [383], [267], [367], [53],
        # [373], [388], [249], [], [], [], []]
        # expected: [null,null,null,null,null,null,null,null,null,29,177,154,471,null,null,null,null,null,null,null,null,249,388,373,53]
        # output:   [null,null,null,null,null,null,null,null,null,29,177,154,471,null,null,null,null,null,null,null,null,249,388,373,333]
        dinnerPlates = DinnerPlates(2)
        dinnerPlates.push(471)
        dinnerPlates.push(177)
        dinnerPlates.push(1)
        dinnerPlates.push(29)
        dinnerPlates.push(333)
        dinnerPlates.push(154)
        dinnerPlates.push(130)
        dinnerPlates.push(333)
        self.assertEqual(29, dinnerPlates.popAtStack(1))
        self.assertEqual(177, dinnerPlates.popAtStack(0))
        self.assertEqual(154, dinnerPlates.popAtStack(2))
        self.assertEqual(471, dinnerPlates.popAtStack(0))
        dinnerPlates.push(165)
        dinnerPlates.push(383)
        dinnerPlates.push(267)
        dinnerPlates.push(367)
        dinnerPlates.push(53)
        dinnerPlates.push(373)
        dinnerPlates.push(388)
        dinnerPlates.push(249)
        self.assertEqual(249, dinnerPlates.pop())
        self.assertEqual(388, dinnerPlates.pop())
        self.assertEqual(373, dinnerPlates.pop())
        self.assertEqual(53, dinnerPlates.pop())

        return

if __name__ == '__main__':
    unittest.main()