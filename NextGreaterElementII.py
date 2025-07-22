class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [-1]*len(nums)
        stack = []
        for _ in range(2):
            for i,num in enumerate(nums):
                while stack and num>nums[stack[-1]]:
                    prev = stack.pop()
                    res[prev] = num
                if res[i] != -1:
                    continue
                stack.append(i)
        return res
