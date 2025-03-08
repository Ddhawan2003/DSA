class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i,j = 0, 0
        max_nums = 0
        if not nums.count(1):
            return 0
        while j<len(nums) and i<len(nums):
            if nums[i]!=1:
                i+=1
                j=i+1
                continue
            if nums[j]!=1:
                max_nums = max(max_nums, j-i)
                i=j+1
                j=i+1
            else:
                j+=1
        return max(max_nums, j-i)
            
        