#LeetCode 28. Find the Index of the First Occurrence in a String
def strStr_bruteforce(haystack: str, needle: str) -> int:
    if not needle:
        return 0

    hay, need = len(haystack), len(needle)
    for i in range(hay-need): #loop over all possible starting indices in haystack where needle could fit
        if haystack[i:i+need] == needle:
            return i
    return -1

print(strStr_bruteforce("I am happy", "am"))