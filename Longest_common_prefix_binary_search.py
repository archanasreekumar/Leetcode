class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return 0

        min_length = min(len(s) for s in strs)
        low, high = 1, min_length

        while low <= high:
            mid = (low + high) // 2
            prefix = strs[0][:mid]
            if all(s.startswith(prefix) for s in strs):
                low = mid + 1
            else:
                high = mid - 1

        return strs[0][:(low + high) // 2]
