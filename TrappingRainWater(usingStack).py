class Solution(object):
    def trap(self,height):
        stack = []
        water = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                bottom = stack.pop()
                if stack: 
                    left = stack[-1]
                    print(bottom,left)
                    h = min(height[i], height[left]) - height[bottom]
                    w = i - left - 1
                    print(h*w)
                    water += h * w
            stack.append(i)
        return water
