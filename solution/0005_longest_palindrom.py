class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        pal_str = ""
        n = len(s)

        for i in range(n):
            # -------- Odd length palindrome (center at i) --------
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > len(pal_str):
                    pal_str = s[l:r+1]
                l -= 1
                r += 1

            # -------- Even length palindrome (center between i and i+1) --------
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > len(pal_str):
                    pal_str = s[l:r+1]
                l -= 1
                r += 1

        return pal_str

        
if __name__ == "__main__":
    # Input: s = "babad"
    # Output: "bab"
    obj = Solution()
    print(obj.longestPalindrome(s = "addab"))