class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        actual_sum=0
        temp_sum=0
        i=0
        for i in range(1, len(nums) + 1):
            actual_sum += i
        for n in nums:
            temp_sum+=n
        return actual_sum-temp_sum
        # if len(nums)==1:
        #     return 1-nums[0]
        # nums.sort()
        # if nums[0] != 0:
        #     return 0
        # for i in range(0, len(nums)-1):
        #     if nums[i] != nums[i+1]-1:
        #         return nums[i+1]-1
        # return len(nums)
        