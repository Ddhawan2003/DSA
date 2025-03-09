class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            # count = [0] * 26  # ✅ Fixed-size array for character counts
            # for char in s:
            #     count[ord(char) - ord('a')] += 1  # ✅ Map 'a' -> 0, 'b' -> 1, etc.
            # res[tuple(count)].append(s)  # ✅ Use tuple as key
            temp=''.join(sorted(s))
            res[temp].append(s)
        return list(res.values())
        