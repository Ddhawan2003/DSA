class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maps = defaultdict(int)
        for n in nums:
            maps[n]+=1
        i=0
        res=[]
        while i < k:
            max_e = max(maps, key=maps.get)
            res.append(max_e)
            del maps[max(maps, key=maps.get)]
            i+=1
        return res

        