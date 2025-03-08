class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_ht = 0
        sums=0
        for g in gain:
            sums+=g
            max_ht=max(max_ht,sums)
        return max_ht
        