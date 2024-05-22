class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # temp = nums[0]
        # for i in range(1, len(nums)):
        #     if nums[i] == temp:
        #         for j in range(i, len(nums)):
        #             if j != len(nums)-1:
        #                 nums[j] = nums[j+1]
        #     temp = nums[i]
        # return len(nums)
        temp = nums[0]
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i] != temp:
                cnt+=1
            temp = nums[i]
        x = 1
        first = 0
        j = 1
        while x < cnt:
            if nums[j] != nums[first]:
                del nums[first+1:j]
                j = first + 1  # Reset j to the position after first
                first += 1
                x += 1
            else:
                j+=1
        return cnt

        