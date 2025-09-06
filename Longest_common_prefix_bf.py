class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return 0

        prefix = strs[0]
        for i in range(len(prefix)):
            for s in strs[1:]:
                if s[i] != prefix[i] or i >= len(s):
                    return prefix[:i]  # return common prefix OR "" if mismatch at first char

        return prefix
