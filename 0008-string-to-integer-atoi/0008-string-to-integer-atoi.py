class Solution:
    def myAtoi(self, s: str) -> int:
        maxI=2**31-1
        minI=(-2)**31
        sign = 1
        res = ''
        flag=1
        s = s.lstrip()
        if not s:
            return 0
        for c in s:
            if flag:
                if c == "-":
                    sign = -1
                    flag = 0
                elif not c.isdigit():
                    if c == "+":
                        flag=0
                        continue
                    break
                else:
                    flag=0
                    res+=c
            else:
                if c.isdigit():
                    res+=c
                else:
                    break
        if res:
            res = int(res)
        else:
            return 0
        if sign*res > maxI:
            res=maxI
        elif sign*res < minI:
            res = abs(minI)
        return sign*res
