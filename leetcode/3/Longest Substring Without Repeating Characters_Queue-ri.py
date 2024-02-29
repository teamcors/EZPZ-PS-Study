from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        chars = set()
        l = 0

        for r in range(len(s)):
            if s[r] not in chars:
                chars.add(s[r])
                maxlen = max(maxlen, r-l+1)
            else:
                while s[r] in chars:
                    chars.remove(s[l])
                    l += 1
                chars.add(s[r])
        
        return maxlen
