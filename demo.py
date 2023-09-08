# import functools
# class Solution:
#     def minNumber(self, nums: [int]) -> str :
#         def cmp(a,b):
#             if a+b==b+a:
#                 return 0
#             elif a + b > b + a:
#                 return 1
#             else:
#                 return -1
#         nums_s=list(map(str,nums))
#         nums_s.sort(key=functools.cmp_to_key(cmp))
#         return ''.join(nums_s)
# list1=[3,30,34,5,9]
# ans=Solution()
# print(ans.minNumber(list1))

