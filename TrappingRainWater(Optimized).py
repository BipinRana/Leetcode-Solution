class Solution(object):
    def trap(self,height):
        stack = []
        water = 0
        for i in range(len(height)):
            while stack and height[i]>height[stack[-1]]:
                bottom = stack.pop()
                if stack:
                    width = i-stack[-1]-1
                    height_diff = min(height[stack[-1]],height[i])-height[bottom]
                    water+= width*height_diff
            stack.append(i)
        return water
