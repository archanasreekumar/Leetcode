class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return 0
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for ch in s:
            if ch in mapping:
                if stack and stack[-1] == mapping[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)

        return stack == []


sol = Solution()
print(sol.isValid("[()([])]"))
