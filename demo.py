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

# class Solustion1:
#     def moveZeroes(self,nums:[int]) -> None:
#         slow=0
#         fast=0
#
#         while fast<len(nums):
#             if nums[fast]!=0:
#                 nums[slow],nums[fast]=nums[fast],nums[slow]
#                 slow+=1
#             fast+=1
#
# ans=Solustion1()
# list1=[1,2,0,3,4]
# list2=ans.moveZeroes(list1)
# print(list2)

