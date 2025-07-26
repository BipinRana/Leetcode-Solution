class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = -float('inf')
        curr_sum = 0
        for right in nums:
            curr_sum +=right
            max_sum = max(max_sum,curr_sum)
            if curr_sum<0:
                curr_sum = 0
        return max_sum
        
