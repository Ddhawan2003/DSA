class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr, l,m,r):
            left = arr[l:m+1]
            right = arr[m+1:r+1]
            i,j,k = l, 0, 0

            while j<len(left) and k<len(right):
                if left[j]<=right[k]:
                    arr[i]=left[j]
                    j+=1
                else:
                    arr[i]=right[k]
                    k+=1
                i+=1
            while j < len(left):
                arr[i]=left[j]
                i+=1
                j+=1
            while k < len(right):
                arr[i]=right[k]
                i+=1
                k+=1
            return arr

        def mergeSort(arr, l,r):
            if l==r:
                return arr
            m=(l+r)//2
            mergeSort(arr, l, m)
            mergeSort(arr, m+1, r)
            merge(arr, l, m, r)
            return arr

        return mergeSort(nums, 0, len(nums)-1)

        