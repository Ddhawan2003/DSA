class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0]= nums[0]
        # dp[1]= max(nums[0], nums[1])
        total_max = dp[0]

        for i in range(1,n):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            if dp[i] > total_max:
                total_max = dp[i]
        return total_max
        