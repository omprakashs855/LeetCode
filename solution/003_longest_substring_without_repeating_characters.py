# Sliding Window Concept

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        longest = 0
        sett = set()
        n = len(s)

        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            
            w = (r - l) + 1
            longest = max(longest, w)
            sett.add(s[r])

        return longest

if __name__ == "__main__":
    obj = Solution()
    # s = "abcabcbb" # 3
    s = "au"
    # s = "bbbbb" # 1
    # s = "pwwkew" # 3

    print(obj.lengthOfLongestSubstring(s))