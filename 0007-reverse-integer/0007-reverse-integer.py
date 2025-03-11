class Solution:
    def reverse(self, x: int) -> int:
        maxI = 2**31-1
        minI=(-2)**31
        rev=0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x > 0:
            dig = x%10
            if rev > (maxI-dig)//10 or rev < (minI-dig)//10:
                return 0
            x//=10
            rev = rev*10+dig
        return sign * rev

        