# Question:

# 2975. Maximum Square Area by Removing Fences From a Field

# There is a large (m - 1) x (n - 1) rectangular field with corners at (1, 1) and (m, n) 
# containing some horizontal and vertical fences given in arrays hFences and vFences respectively.

# Horizontal fences are from the coordinates (hFences[i], 1) to (hFences[i], n) and 
# vertical fences are from the coordinates (1, vFences[i]) to (m, vFences[i]).

# Return the maximum area of a square field that can be formed by removing some 
# fences (possibly none) or -1 if it is impossible to make a square field.

# Since the answer may be large, return it modulo 10^9 + 7.

# Note: The field is surrounded by two horizontal fences from the coordinates (1, 1) to (1, n) and (m, 1) to (m, n) and two vertical fences from the coordinates (1, 1) to (m, 1) and (1, n) to (m, n). These fences cannot be removed.

from typing import List


class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10**9 + 7
        
        h_list = [1] + hFences + [m]
        v_list = [1] + vFences + [n]
        
        h_list.sort()
        v_list.sort()
        
        h_len = set()
        
        # All horizontal distances
        for i in range(len(h_list)):
            for j in range(i + 1, len(h_list)):
                h_len.add(h_list[j] - h_list[i])
        
        dist = 0
        
        # Find largest matching vertical distance
        for i in range(len(v_list)):
            for j in range(i + 1, len(v_list)):
                d = v_list[j] - v_list[i]
                if d in h_len:
                    dist = max(dist, d)
        
        return (dist * dist) % MOD if dist > 0 else -1
