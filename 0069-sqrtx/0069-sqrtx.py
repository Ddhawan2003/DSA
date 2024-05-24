class Solution:
    def mySqrt(self, x: int) -> int:
        i=1
        while i <= x:
            if i*i > x:
                return i-1
            if i*i == x:
                return i
            i+=1
        return 0
