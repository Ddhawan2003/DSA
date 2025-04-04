class Solution:
    def trap(self, height: List[int]) -> int:
        # sum_w = 0
        # for i in range(len(height)):
        #     leftM = rightM = height[i]

        #     for x in range(i):
        #         leftM = max(leftM, height[x])
        #     for y in range(i+1, len(height)):
        #         rightM = max(rightM, height[y])

        #     sum_w+= max(0, min(leftM, rightM) - height[i])

        # return sum_w
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1

        return water
        