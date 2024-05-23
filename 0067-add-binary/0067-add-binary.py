class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        num1 = 0
        cnt = 0
        i=len(a)-1
        j=len(b)-1
        while i >= 0:
            num1=num1+(int(a[i])*(2**cnt))
            cnt+=1
            i-=1
        num2 = 0
        cnt = 0
        while j >= 0:
            num2=num2+(int(b[j])*(2**cnt))
            cnt+=1
            j-=1
        sum = num1+num2
        if sum == 0:
            return "0"
        result = ""
        while sum > 0:
            result = str(sum%2) + result
            sum/=2 
        return result
        