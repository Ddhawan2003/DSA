class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,h=0,len(nums)-1
        temp = -1
        while l<=h:
            m=(l+h)//2
            if nums[m] == target:
                temp = m
                h = m - 1
            elif nums[m] < target:
                l=m+1
            else:
                h=m-1
        if temp == -1:
            return [-1,-1]
        else:
            arr = []
            for i in range(temp,len(nums)):
                if nums[temp] == nums[i]:
                    arr.append(i)
            return [temp, arr[len(arr)-1]]