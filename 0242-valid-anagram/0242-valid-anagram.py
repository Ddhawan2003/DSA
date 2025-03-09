class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen1={}
        seen2={}
        for i in s:
            seen1[i]=1+seen1.get(i, 0)
        for i in t:
            seen2[i]=1+seen2.get(i, 0)
        return seen1==seen2
        