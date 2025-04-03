class Solution:
    def canJump(self, nums: List[int]) -> bool:
        leng = 0
        for n in nums:
            if leng < 0:
                return False
            elif n > leng:
                leng = n
            leng -= 1
            
        return True