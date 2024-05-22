class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        h = len(nums) - 1
        while l <= h:
            mid = (l+h)//2
            if nums[mid] < target:
                l=mid+1
            elif nums[mid] > target:
                h=mid-1
            else:
                return mid
        return l
        