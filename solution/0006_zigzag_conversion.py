# Zigzag Conversion

class Solution:
    def convert(self, s:str, numRows:int) -> str:
        if numRows < 2:
            return s
        else:
            out_str = ""
            data = {}
            for idx in range(numRows):
                data[idx] = ""

                n = len(s)
                i = 0

                gap = 2*numRows - 2

                if idx > 0 and idx < (numRows-1):
                    inner_gap = gap-2*idx
                else:
                    inner_gap = 0

                while True:
                    if (i+idx) < n:
                        
                        data[idx] += s[i + idx]

                        if i+idx+inner_gap < n and idx > 0 and idx < (numRows-1):
                            data[idx] += s[i + idx + inner_gap]

                        i += gap
                    else:
                        break
            out_str = "".join([x for x in data.values()])
            return out_str




obj = Solution()
print(obj.convert(s = "PAYPALISHIRING", numRows = 10))