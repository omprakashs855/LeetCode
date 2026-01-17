class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            inv = 0
            val = x
            while val:
                rem = val%10
                val = val//10
                inv = inv*10 + rem
            
            if inv == x:
                return True
            else:
                return False
        