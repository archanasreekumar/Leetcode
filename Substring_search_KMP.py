class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        # Step 1: Build LPS table for needle
        lps = [0] * len(needle)
        i, prev = 1, 0
        while i < len(needle):
            if needle[i] == needle[prev]:
                prev += 1
                lps[i] = prev
                i += 1
            elif prev > 0:
                prev = lps[prev - 1]
            else:
                lps[i] = 0
                i += 1

        # Step 2: Search using LPS
        i = j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    return i - j  # match found
            else:
                if j > 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return -1
