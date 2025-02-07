class Solution:
    def isPalindrome(self, x: int) -> bool:
        # copy = x
        # rev = ''
        # if x == 0:
        #     return True
        # while copy > 0:
        #     dig=copy%10
        #     rev+=str(dig)
        #     copy//=10
        # print(rev)
        # if rev == str(x):
        #     return True
        # return False
        # copy = x
        # if copy == 0:
        #     return True
        # num = ''
        # while copy > 0:
        #     dig = copy%10
        #     num+=str(dig)
        #     copy//=10
        # if num == str(x):
        #     return True
        # else:
        #     return False
        num = str(x)
        return str(x) == num[::-1]