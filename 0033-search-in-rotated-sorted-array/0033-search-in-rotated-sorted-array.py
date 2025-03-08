class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,h = 0, len(nums)-1
        temp = nums[0]
        while l<=h:
            m=(l+h)//2
            if nums[m] == target:
                return m
            if nums[m] < temp:
                h=m-1
            else:
                l=m+1
        if l < len(nums):
            pivoting = l
        else:
            pivoting = 0
        print(pivoting)
        if target > nums[len(nums)-1]:
            l=0
            h=pivoting-1
        elif target < nums[len(nums)-1]:
            l=pivoting 
            h=len(nums)-1
        else:
            return len(nums)-1
        while l<=h:
            m=(l+h)//2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                h=m-1
            else:
                l=m+1
        return -1
                