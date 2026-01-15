# Zigzag Conversion

class Solution:
    def convert(self, s:str, numRows:int) -> str:
        if numRows < 2:
            return s
        else:
            data = {}
            for idx in range(numRows):
                data[idx] = ""

                gap = 2*numRows - 2
                n = len(s)
                i = 0

                while True:
                    if (i+idx) < n:
                        data[idx] += s[i + idx]
                        i += gap
                    else:
                        break

            print(data)

            return "".join([x for x in data.values()])




obj = Solution()
print(obj.convert(s = "PAYPALISHIRING", numRows = 5))