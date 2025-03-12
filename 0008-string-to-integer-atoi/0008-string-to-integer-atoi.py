class Solution:
    def myAtoi(self, s: str) -> int:
        maxI=2**31-1
        minI=(-2)**31
        sign = 1
        res = []
        flag=True
        s = s.lstrip()
        if not s:
            return 0
        # for c in s:
        #     if flag:
        #         if c == "-":
        #             sign = -1
        #             flag = 0
        #         elif not c.isdigit():
        #             if c == "+":
        #                 flag=0
        #                 continue
        #             break
        #         else:
        #             flag=0
        #             res+=c
        #     else:
        #         if c.isdigit():
        #             res+=c
        #         else:
        #             break
        i = 0
        if s[i] in "+-":
            sign = -1 if s[i] == '-' else 1
            i += 1
        while i < len(s) and s[i].isdigit():
            res.append(s[i])
            i += 1
        if not res:
            return 0
        res = int(''.join(res)) * sign
        if res > maxI:
            return maxI
        if res < minI:
            return minI
        return res
