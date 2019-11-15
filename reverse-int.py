import re
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        l = list(str(x))
        l.reverse()
        while l[0] == '0':
            l.pop(0)
        if l[-1] == '-':
            l.insert(0,'-')
            l.pop()
        if x < -2 ** 31 or x > 2 ** 31 - 1:
            return 0
        return int(''.join(l))
a=Solution()
print(a.reverse(1534236469))