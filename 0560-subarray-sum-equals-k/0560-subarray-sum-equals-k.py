class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = {0: 1}
        run_sum = 0
        res = 0
        for i in range(0, len(nums)):
            run_sum+=nums[i]
            if (run_sum-k) in prefix_map:
                res+=prefix_map.get(run_sum-k, 0)
            prefix_map[run_sum] = prefix_map.get(run_sum, 0) + 1
        return res

#         # h=0
#         # run_sum = 0
#         # res=0
#         # if k == nums[-1]:
#         #     res+=1
#         # while h < len(nums):
#         #     run_sum+=nums[h]
#         #     if run_sum==k:
#         #         res+=1
#         #         run_sum=0
#         #     else:
#         #         h+=1
#         # return res

#         i=0
#         res=0
#         run_sum=0
#         if k == nums[-1]:
#             res+=1
#         while i < len(nums):
#             run_sum+=nums[i]
#             if run_sum == k:
#                 run_sum=0
#                 res+=1
#             else:
#                 i+=1
#         return res