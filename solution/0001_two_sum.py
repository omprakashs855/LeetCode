# TWO SUMS Solution

from typing import List

# Brute Force Class
class Solution_BruteForce:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)

        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i,j]

        return []

# Two Pass Hash Class
class Solution_Two_Pass_Hash_Table:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numMap = {}
        n = len(nums)

        for i in range(n):
            numMap[nums[i]] = i

        for i in range(n):
            diff = target - nums[i]
            if diff in numMap and numMap[diff] != i:
                return [numMap[diff], i]

        return []

# One Pass Hash Table
class Solution_One_Pass_Hash_Table:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}
        for idx, val in enumerate(nums):
            diff = target - val

            if val in seen:
                return [seen[val], idx]
            else:
                seen[diff] = idx
        return []

# obj1 = Solution_BruteForce()
# print(obj1.twoSum(nums = [2,7,11,15], target = 9))

# obj2 = Solution_Two_Pass_Hash_Table()
# print(obj2.twoSum(nums = [2,7,11,15], target = 9))

obj3 = Solution_One_Pass_Hash_Table()
print(obj3.twoSum(nums = [2,7,11,15], target = 9))

# To Run : python solution/0001_two_sum.py from root directory 