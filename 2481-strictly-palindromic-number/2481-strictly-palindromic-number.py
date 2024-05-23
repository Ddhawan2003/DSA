class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        if n%2 == 0:
            return False
        base = 2
        n = str(n)
        cnt = 0
        while base <= (int(n)-2):
            i = len(n) - 1
            num = 0
            while i >= 0:
                num=num+(int(n[i])*(base**cnt))
                cnt+=1
                i-=1
            if not self.isPal(num):
                return False
            base+=1
        return True
    
    def isPal(self, num):
            rev = 0
            copy = num
            while num > 0:
                rev = rev + num%10
                num/=10
            if rev == copy:
                return True
            return False