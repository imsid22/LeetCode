from typing import List
from dataclasses import dataclass

@dataclass
class Solution:
    nums: List[int]

    def maxSubArray(self) -> int:
        maxsum = 0
        for i in range(len(self.nums)):
            for j in range(len(self.nums)):
                if sum(self.nums[i:j+1]) > maxsum:
                    maxsum = sum(self.nums[i:j+1])
        return maxsum


if __name__ == "__main__":
    arr = [5,4,-1,7,8]
    solution = Solution(arr)
    print(solution.maxSubArray())