class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for i in num:
            while stack and i < stack[-1] and k:
                stack.pop()
                k -= 1
            stack.append(i)

        stack = stack[:-k] if k else stack

        output = (''.join(stack)).lstrip('0')

        return output if output else '0'
