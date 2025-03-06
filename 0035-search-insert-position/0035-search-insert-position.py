class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums)-1
        if target < nums[0]:
            return 0
        if target > nums[len(nums)-1]:
            return len(nums)
        while l < h:
            m = math.ceil((l+h)/2)
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l=m+1
            else:
                h=m-1
        if l == h:
            return l+1 if nums[l] < target else l
        return m+1