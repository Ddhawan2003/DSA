class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        cnt = 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                cnt+=1
                nums.pop(i)
                i-=1
            i+=1
        print(nums)
        return (length-cnt)
        # j = 0
        # while x < len(nums) - cnt:
        #     if nums[j] == temp:
        #         nums.pop(j)
        #     else:
        #         j+=1