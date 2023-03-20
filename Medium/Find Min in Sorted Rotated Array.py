from typing import List
from dataclasses import dataclass

@dataclass
class Solution:
    nums: List[int]

    def findMin(self) -> int:
        min_num = self.nums[0]
        hi = len(self.nums) - 1
        lo = 0
        while hi > lo:
            mid = (hi + lo) // 2
            if self.nums[mid] > self.nums[hi]:
                min_num = self.nums[hi]
                lo = mid + 1
            else:
                hi = mid
                min_num = self.nums[mid]

        return min_num


if __name__ == "__main__":
    arr = [4,5,6,7,0,1,2]
    solution = Solution(arr)
    print(solution.findMin())

