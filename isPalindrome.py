class Solution:
    def isPalindrome(self, x: int) -> bool:
        a=list(str(x))
        b = a.copy()
        b.reverse()
        print(a,b)
        if a == b:
            return True
        else:
            return False


s = Solution()
print(s.isPalindrome(-121))