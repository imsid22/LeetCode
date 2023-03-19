from typing import List
from dataclasses import dataclass
import math

@dataclass
class Solution:
    nums: List[int]

    def maxSubArray(self) -> int:
        maxsum = -1*math.inf
        for i in range(len(self.nums)):
            for j in range(i, len(self.nums)):
                if sum(self.nums[i:j+1]) > maxsum:
                    maxsum = sum(self.nums[i:j+1])
        return maxsum


if __name__ == "__main__":
    arr = [-2, -1]
    solution = Solution(arr)
    print(solution.maxSubArray())