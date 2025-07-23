class Solution(object):
    def mostCompetitive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        stack = []
        length = len(nums)
        for i,num in enumerate(nums):
            while stack and (length-i> k) and num<stack[-1]:
                stack.pop()
                length -= 1
            stack.append(num)
            length+=1

        return stack if len(stack)==k else stack[:k]
