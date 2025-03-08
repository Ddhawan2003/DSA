class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            prev = merged[-1]
            curr = intervals[i]

            if curr[0] <= prev[1]:
                prev[1] = max(prev[1], curr[1])
            else:
                merged.append(curr)
            i+=1
        return merged

        # temp = []
        # i = 0
        # j = 0
        # intervals.sort()
        # while i < len(intervals):
        #     start = intervals[i][0]
        #     target = intervals[i][1]
        #     if i == len(intervals)-1:
        #         temp.append([start, target])
        #         break
        #     while i < len(intervals)-1 and target >= intervals[i+1][j]:
        #         j+=1
        #         # target = intervals[i+1][j]
        #         if j == 2:
        #             j=0
        #             i+=1
        #             target = intervals[i+1][j]
        #         if target < max(target, intervals[i+1][j]):
        #             target = max(target, intervals[i+1][j])
        #             i+=1
        #     temp.append([start, target])
        #     i+=1
        # return temp


        