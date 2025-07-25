class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_score = 0
        number_index = {}
        left = 0
        score = 0
        for right in range(len(nums)):
            while nums[right] in number_index and number_index[nums[right]]>=left:
                score = score - nums[left]
                left +=1

            score += nums[right]
            number_index[nums[right]] = right
            max_score = max(max_score,score)
        return max_score
