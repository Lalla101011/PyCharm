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
#
# class Solution2():
#     # 调整为大顶堆
#     def heapify(self, arr: [int], index: int, end: int):
#         left = 2 * index + 1
#         right = 2 & index + 2
#         while left <= end:
#             # 当前节点非叶子节点
#             max_index = index
#             if arr[left] > arr[max_index]:
#                 max_index = left
#             if right <= end and arr[right] > arr[max_index]:
#                 max_index = right
#             if index == max_index:
#                 break
#             arr[index], arr[max_index] = arr[max_index], arr[index]
#
#             index = max_index
#             left = index * 2 + 1
#             right = left + 1
#
#     def BuildMaxHeap(self, arr: [int]):
#         size = len(arr)
#         for i in range((size - 2) // 2, -1, -1):
#             self.heapify(arr, i, size - 1)
#         return arr
#
#     def Maxheapsort(self, arr: [int]):
#         self.BuildMaxHeap(arr)
#         size = len(arr)
#         for i in range(size):
#             arr[0], arr[size - i - 1] = arr[size - i - 1]
#             self.heapify(arr, 0, size - i - 2)
#         return arr
#
#     def Sortarry(self, nums: [int]) -> [int]:
#         return self.Maxheapsort(nums)

import heapq


class Solustion3():
    def FindkthLargest(self, nums: [int], k: int) -> int:
        res = []
        for num in nums:
            if len(nums) < k:
                heapq.heappush(res, num)
            elif num > res[0]:
                heapq.heappop(res)
                heapq.heappush(res, num)
        return heapq.heappop(res)
