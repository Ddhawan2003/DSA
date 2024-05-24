class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        while i < m + len(nums2) and nums2:
            if nums2[j] <= nums1[i]:
                nums1.insert(i,nums2[j])
                nums2.pop(j)
                nums1.pop(len(nums1)-1) 
                m+=1
            else:
                i+=1
        if nums2:
            x=1
            while x <= len(nums2):
                nums1.pop(len(nums1)-1)
                x+=1
            nums1.extend(nums2)
        
        