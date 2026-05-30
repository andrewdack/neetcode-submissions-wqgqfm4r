class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n
        seen = {}
        l, r, maxLen = 0, 0, 0
        while l < n and r < n:
            char = s[r]
            # new unique character we havent seen
            if char not in seen:
                seen[char] = r
            # this is a duplicate character
            else:
                l = max(l, seen[char] + 1)
                seen[char] = r
            
            r += 1
            maxLen = max(maxLen, r - l)
        
        return maxLen
        