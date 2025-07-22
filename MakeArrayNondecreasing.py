class Solution(object):
    def maximumPossibleSize(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        biggest = 0
        count = 0
        for num in nums:
                if num>= biggest:
                    biggest = num
                    count +=1
        return count      
                
