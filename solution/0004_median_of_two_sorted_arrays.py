from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m = len(nums1)
        n = len(nums2)
        half = (m + n + 1)//2

        # partition nums1 only (smaller array/list)
        low = 0
        high = m

        while low <= high:

            i = (low + high)//2
            j = half - i

            # handling edge conditions
            leftA = float('-inf') if i == 0 else nums1[i-1]
            rightA = float('inf') if i == m else nums1[i]

            leftB = float('-inf') if j == 0 else nums2[j-1]
            rightB = float('inf') if j == n else nums2[j]

            if leftA <= rightB and leftB <= rightA:
                # print("leftA {}, leftB {} | rightA {}, rightB {}". \
                # format(leftA, leftB, rightA, rightB))
                if (m+n)%2 != 0:
                    return max(leftA, leftB)
                else:
                    return (max(leftA, leftB) + min(rightA, rightB))/2
            elif leftA > rightB:
                high = i-1
            elif leftB > rightA:
                low = i+1
        
if __name__ == "__main__":
    nums1, nums2 = [1,2], [3,4]
    obj = Solution()
    print(obj.findMedianSortedArrays(nums1, nums2))
    