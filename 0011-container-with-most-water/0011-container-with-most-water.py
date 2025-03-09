class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,h=0, len(height)-1
        max_area = 0
        while l<h:
            max_area = max(max_area, (h-l)*min(height[l],height[h]))
            if height[l] < height[h]:
                l+=1
            else:
                h-=1
        return max_area
        