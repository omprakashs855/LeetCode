# Zigzag Conversion

class Solution:
    def convert_math(self, s:str, numRows:int) -> str:
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

    # Most Fastest # Less Math
    def convert(self, s, numRows):
        if numRows < 2:
            return s
        else:

            rows = [""]*numRows
            direction = 1 # down
            cur = 0

            for i in range(len(s)):

                rows[cur] += s[i]
                if cur == 0:
                    direction = 1
                elif cur == numRows-1:
                    direction = -1

                cur += direction

            return "".join(rows)


obj = Solution()
s = "PAYPALISHIRING"
numRows = 4
print(obj.convert(s, numRows))
print(obj.convert_math(s, numRows))