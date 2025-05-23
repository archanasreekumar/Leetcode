https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        length=0
        temp=''
        for i in range(len(s)+1):
            for j in range(i+1,len(s)+1):
                if s[i:j]==s[i:j][::-1]:
                    if len(s[i:j])>length:
                        length=len(s[i:j])
                        temp=s[i:j]
        return temp