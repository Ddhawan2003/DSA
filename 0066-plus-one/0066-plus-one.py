class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # num=0
        # arr = []
        # for d in digits:
        #     num = num*10 + d
        # num+=1
        # for n in str(num):
        #     arr.append(int(n))
        # return arr
        i = len(digits) - 1
        while i >= 0:
            if digits[i] < 9:
                digits[i]+=1
                return digits
            digits[i] = 0
            i-=1
        return [1] + digits

        
        