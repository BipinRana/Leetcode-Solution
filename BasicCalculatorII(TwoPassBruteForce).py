class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        left = 0 
        s = ''.join(s.split())
        while left <len(s):
            if s[left] == " ":
                left+=1
                continue
            if s[left].isnumeric():
                flag =left
                num = int(s[left])
                while left+1< len(s) and s[left+1].isnumeric():
                    num = num*10+int(s[left+1])
                    left+=1
                
                
                if s[flag-1] =="*":
                    stack.pop()
                    stack[-1] = stack[-1]*num
                
                elif s[flag-1] == "/":
                    stack.pop()
                    stack[-1] = stack[-1]/num
                
                else:
                    stack.append(num)
            else:
                stack.append(s[left])   
            left+=1
        
        s_stack = []
        left = 0 
        print(stack)
        while left <len(stack):
            if s_stack and stack[left-1] =="+":
                s_stack.pop()
                s_stack[-1] = s_stack[-1]+stack[left]
                
            elif s_stack and stack[left-1] == "-":
                s_stack.pop()
                s_stack[-1] = s_stack[-1]-stack[left]  
            else:
                s_stack.append(stack[left])
            left+=1
        return s_stack[0]
