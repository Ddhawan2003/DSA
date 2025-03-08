# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         i=0
#         while i < n:
#             if nums[i]==0:
#                 nums.append(nums.pop(i))
#             else:
#                 i+=1
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_count = nums.count(0)  # ✅ Count total zeros

        i = 0
        while zero_count > 0:  # ✅ Run the loop only for existing zeros
            if nums[i] == 0:
                nums.pop(i)  # ✅ Remove the zero
                nums.append(0)  # ✅ Append zero at the end
                zero_count -= 1  # ✅ Decrease count, since a zero was processed
            else:
                i += 1  # ✅ Move forward only if no pop happened
