class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in range(0, len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])
            elif not stack:
                return False
            elif s[i] == ")":
                if stack.pop() != "(":
                    return False 
            elif s[i] == "}":
                if stack.pop() != "{":
                    return False
            elif s[i] == "]":
                if stack.pop() != "[":
                    return False
        if not stack:
            return True
        return False
        