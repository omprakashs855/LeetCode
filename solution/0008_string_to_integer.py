class Solution:
    def myAtoi(self, s: str) -> int:
        int_out = ""
        s = s.strip()
        neg = 1

        if not s:
            return 0
        else:
            s0 = s[0] # first_string
            if (ord(s0) not in range(48, 58)) and (s0 not in ['-', '+']):
                return 0
            else:
                if s[0] == "+":
                    neg = 1
                    s = s[1:]
                elif s[0] == "-":
                    neg = -1
                    s = s[1:]
                
                for i in s:
                    if ord(i) in range(48,58):
                        int_out += i
                    else:
                        break
                if int_out:
                    int_out = int(int_out)*neg
                else:
                    return 0
                    
                if int_out < (-1)*2**31:
                    return (-1)*2**31
                elif int_out > 2**31 - 1:
                    return 2**31 - 1
                else:
                    return int_out
                
    def myAtoi_faster(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        sign = 1
        i = 0
        result = 0

        if s[0] == '+' or s[0] == '-':
            sign = -1 if s[0] == '-' else 1
            i += 1

        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        result *= sign

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        return result
                
s = "+-12"
obj = Solution()
print(obj.myAtoi(s))
print(obj.myAtoi_faster(s)) # This is more cleaner