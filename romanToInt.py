import re
class Solution:
    def getValue(self, s: str) -> int:
        if s == 'I': return 1
        if s == 'V': return 5
        if s == 'X': return 10
        if s == 'L': return 50
        if s == 'C': return 100
        if s == 'D': return 500
        if s == 'M': return 1000

    def romanToInt(self, s: str) -> int:
        sum = 0
        l = list(s)
        preNum = 0
        for i in range(len(l)):
            num = self.getValue(l[i])
            if preNum < num:
                sum  -= preNum
            else:
                sum += preNum
            preNum = num
        print(sum)
        sum += preNum
        return sum
x = Solution()
print(x.romanToInt('XXXVII'))