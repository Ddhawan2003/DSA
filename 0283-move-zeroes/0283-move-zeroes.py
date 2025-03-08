class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0  # ✅ Pointer for the next non-zero position

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[start] = nums[i]  # ✅ Move non-zero forward
                start += 1  # ✅ Move the write pointer

        # ✅ Fill remaining positions with zeros
        for i in range(start, len(nums)):
            nums[i] = 0





        