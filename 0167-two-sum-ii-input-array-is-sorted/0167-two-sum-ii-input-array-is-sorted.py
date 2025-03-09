class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        freq = defaultdict(int)
        for i,n in enumerate(numbers):
            diff = target-n
            if diff in freq and freq[diff] != i+1:
                return [freq[diff], i+1]
            freq[n]=i+1
        return []
        