class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = []
        i = 0
        j = 0
        maxLen=0
        substr=[]
        if len(s) == 0:
            return 0  # Handle edge case for empty string
        if len(s) == 1:
            return 1  # Handle single-character strings
        while j < len(s):
            if s[j] not in temp:
                temp.append(s[j])
                j+=1
                if maxLen < (j-i):
                    maxLen=(j-i)
                    substr=s[i:j]
            else: 
                while s[j] in temp:
                    temp.pop(0)
                    i+=1
        print(substr)
        return maxLen

            
            