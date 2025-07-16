class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = 1
        internal_sum= 0
        output = 0
        containers = set()
        while len(height)>right:
            if height[left]>height[right]:
                internal_sum+=height[right]
                right+=1   
            else:
                max_water = min([height[right],height[left]])*(right-left-1)
                
                output+= max_water - internal_sum
                containers.add((left,right))
                internal_sum=0
                left=right
                right+=1       
        left=len(height)-2
        right=len(height)-1
        internal_sum=0
        while 0<=left:
            if height[left]<height[right]:
                internal_sum+=height[left]
                left-=1   
            else:
                max_water = min([height[right],height[left]])*(right-left-1)
                if (left,right) not in containers:
                    output+= max_water - internal_sum
                    containers.add((left,right))
                internal_sum=0
                
                right = left
                left-=1        
        return output  
        

