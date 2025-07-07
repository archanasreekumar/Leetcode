#https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen= {}  # char → last index
        l = 0                           # left pointer
        ans = 0

        for r, ch in enumerate(s):      # right pointer
            if ch in last_seen and last_seen[ch] >= l:
                l = last_seen[ch] + 1   # move left past duplicate
            last_seen[ch] = r           # update last seen
            ans = max(ans, r - l + 1)   # current window length

        return ans
