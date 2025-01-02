class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # left = 0
        # right = len(nums)-1
        # while left <= right:
        #     if nums[left] + nums[right] == target:
        #         break
        #     elif abs(nums[left]) + abs(nums[right]) < abs(target):
        #         left+=1
        #     else:
        #         right-=1
        # return [left, right]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

        