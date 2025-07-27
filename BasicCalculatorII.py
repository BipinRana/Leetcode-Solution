class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for token in s:
            if token == " ":
                continue
            if not stack:
                stack.append(int(token))
                continue
            if token.isnumeric():
                token = int(token)
                if stack[-1].isnumeric():
                    stack[-1] = stack[-1]*10+token
            if stack[-1] == '*':
                stack.pop()
                stack[-1] = stack[-1]*(token)
            elif stack[-1] =="/":
                stack.pop()
                stack[-1] = stack[-1]/(token)
            else:
                stack.append(token)
        
        s_stack =[]
        for token in stack:
            if not s_stack:
                s_stack.append(token)
                continue
            if s_stack[-1] == '+':
                s_stack.pop()
                print(s_stack[-1],token)
                s_stack[-1] = s_stack[-1]+(token)
            elif s_stack[-1] =="-":
                s_stack.pop()
                s_stack[-1] = s_stack[-1]-(token)
            else:
                s_stack.append(token)
        return s_stack[0]






           
