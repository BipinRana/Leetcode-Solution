class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for character in s:
            if character in "({[":
                stack.append(character)
            elif not stack and character in "}])":
                return False
            elif (character==")" and stack[-1] =="(") or (character=="}" and stack[-1] =="{") or (character=="]" and stack[-1] =="["):
                stack.pop()
            else:
                return False
        if stack:
            return False
        else:
            return True
        
