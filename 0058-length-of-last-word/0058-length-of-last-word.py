class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s)-1
        j = 0
        start = len(s)
        while i >= 0:
            if s[i] != " ":
                start = i
                j = i
                while j >= 0:
                    if s[j] == " ":
                        return start - j
                    j-=1
                return start+1
            i-=1
        return start+1
                      