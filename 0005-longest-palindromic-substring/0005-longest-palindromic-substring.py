class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expandAroundCenter(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        if not s or len(s) == 0:
            return ""

        longest = ""
        for i in range(len(s)):
            # Odd length palindromes (single character center)
            palindrome1 = expandAroundCenter(s, i, i)
            # Even length palindromes (double character center)
            palindrome2 = expandAroundCenter(s, i, i + 1)
            # Update the longest palindrome found
            longest = max(longest, palindrome1, palindrome2, key=len)

        return longest

        