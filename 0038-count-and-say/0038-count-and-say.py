class Solution:
    def countAndSay(self, n: int) -> str:
            result = "1"
            for _ in range(1,n):
                res = []
                i=0
                while i < len(result):
                    cnt = 1
                    while i + 1 < len(result) and result[i] == result[i+1]:
                        cnt+=1
                        i+=1
                    res.append(str(cnt))
                    res.append(result[i])
                    i+=1
                result = ''.join(res)

            return result   