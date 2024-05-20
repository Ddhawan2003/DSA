class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(0, len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if (nums[i] + nums[j]) == target:
        #             return [i,j]
        nums_with_index = [(number, index) for index, number in enumerate(nums)]
        nums_with_index.sort(key=lambda x: x[0])
        left = 0
        right = len(nums) - 1
        while left < right:
            current_sum = nums_with_index[left][0] + nums_with_index[right][0]
            if current_sum == target:
                return [nums_with_index[left][1], nums_with_index[right][1]]
            if current_sum < target:
                left = left + 1
            if current_sum > target:
                right = right - 1
