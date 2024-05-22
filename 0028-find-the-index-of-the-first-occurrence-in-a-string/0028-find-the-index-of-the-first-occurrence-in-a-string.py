class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) > len(haystack):
            return -1
        match = False
        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                match = True
                for j in range(1, len(needle)):
                    if haystack[i+j] != needle[j]:
                        match = False
                        break
            if match:
                return i
        return -1
                        


        