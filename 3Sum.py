class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        output=[]
        for i,target in enumerate(nums):
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i+1
            right = len(nums)-1
            while left<right:
                total = target+nums[left]+nums[right]
                if  total >0:
                    right-=1
                elif total <0:
                    left+=1  
                elif total ==0:
                    output.append([target,nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return output            

            
