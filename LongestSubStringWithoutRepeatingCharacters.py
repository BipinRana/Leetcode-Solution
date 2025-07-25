class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dikt = {}
        left = 0
        max_count = 0
        for right in range(len(s)):
            if s[right] in dikt and dikt[s[right]]>=left:
                left = dikt[s[right]]+1
            else:
                max_count = max(max_count,right - left +1)
            dikt[s[right]] = right
        return max_count
