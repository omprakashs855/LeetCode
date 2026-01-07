# TWO SUMS Solution

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}
        for idx, val in enumerate(nums):
            diff = target - val

            if val in seen:
                return [seen[val], idx]
            else:
                seen[diff] = idx

        
obj = Solution()
obj.twoSum(nums = [2,7,11,15], target = 9)

# To Run : python solution/0001_two_sum.py from root directory 