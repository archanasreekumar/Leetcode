https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=str(x)
        if len(y)!=1:
            index=len(y)//2
            if y[:index]==y[-index:][::-1]:
                return True
            else:
                return False
        else:
            return True


