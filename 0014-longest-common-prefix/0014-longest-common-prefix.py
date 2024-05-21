class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        substr = ""
        for i in range(1, len(strs[0]) + 1):
            copy = substr
            substr = strs[0][:i]
            #print(substr)
            for j in range(1, len(strs)):
                if not strs[j].startswith(substr):
                    return copy
        return substr


        