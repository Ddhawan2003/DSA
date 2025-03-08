class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1-nums[0]
        nums.sort()
        if nums[0] != 0:
            return 0
        for i in range(0, len(nums)-1):
            if nums[i] != nums[i+1]-1:
                return nums[i+1]-1
        return len(nums)
        