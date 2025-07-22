class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        stack = []
        length = len(speed)
        for i in range(length):
            temp.append((position[i],speed[i]))
        temp.sort(reverse = True)
        for pos,speed in temp:
            time = (target-pos)/float(speed)            
            if not stack or time>stack[-1]:
                stack.append(time)
        return len(stack)
