class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        left = 0 
        sign = "+"
        while left <len(s):
            if s[left].isdigit():
                num = int(s[left])
                while left+1< len(s) and s[left+1].isdigit():
                    num = num*10+int(s[left+1])
                    left+=1
                
                if sign == "*":
                    stack[-1] *= num
                
                elif sign == "/":
                    temp = stack.pop()
                    stack.append(temp//num)

                elif sign =="+":
                    stack.append(num)

                elif sign =="-":
                    stack.append(-num)

                else:
                    stack.append(num)
            elif s[left] in "*+/-":
                sign = s[left]
            left+=1
        return(sum(stack))
