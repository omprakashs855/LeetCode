class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        else:
            rev_x = ""
            val = abs(x)
            neg = -1 if x < 0 else 1

            while val>0:
                val_r = val%10
                val = val//10
                rev_x += str(val_r)

            rev_x = int(rev_x)*neg
            if rev_x >= (-1)*2**31 and rev_x <= 2**31-1:
                return rev_x
            else:
                return 0

        