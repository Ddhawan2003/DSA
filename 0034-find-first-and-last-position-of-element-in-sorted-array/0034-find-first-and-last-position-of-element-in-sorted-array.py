class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,h=0,len(nums)-1
        temp1 = -1
        while l<=h:
            m=(l+h)//2
            if nums[m] == target:
                temp1 = m
                h = m - 1
            elif nums[m] < target:
                l=m+1
            else:
                h=m-1
        
        l,h=0,len(nums)-1
        temp2 = -1
        while l<=h:
            m=(l+h)//2
            if nums[m] == target:
                temp2 = m
                l = m + 1
            elif nums[m] < target:
                l=m+1
            else:
                h=m-1

        return [temp1, temp2]