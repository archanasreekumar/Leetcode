https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        openlist=[]
        closelist=[]
        if len(s)%2==0:
            for i in range(len(s)):
                if s[i]=="(" or s[i]=="[" or s[i]=="{":
                    openlist.append(s[i])
                if (s[i]==")" or s[i]=="]" or s[i]=="}"):
                    closelist.append(s[i])
                if openlist!=[]:
                    if openlist[-1]+s[i]=="()" or openlist[-1]+s[i]=="[]" or openlist[-1]+s[i]=="{"+"}":
                        openlist=openlist[:-1]
                        closelist=closelist[:-1]
            if openlist==[] and closelist==[]:
                return True
            else:
                return False
        else:
            return False
