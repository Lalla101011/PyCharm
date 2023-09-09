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
#
# import heapq
#
#
# class Solustion3():
#     def FindkthLargest(self, nums: [int], k: int) -> int:
#         res = []
#         for num in nums:
#             if len(nums) < k:
#                 heapq.heappush(res, num)
#             elif num > res[0]:
#                 heapq.heappop(res)
#                 heapq.heappush(res, num)
#         return heapq.heappop(res)
#
# class Solution4():
#     def search(self, nums: [int], target: int) -> int:
#         left = 0
#         right = len(nums) - 1
#         while left <= right:
#             mid = (left + right) // 2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] > target:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         return -1
#
#
# list3 = [-1, 0, 3, 5, 9, 12]
# target = 9
# ans = Solution4()
# print(ans.search(list3, target))
#
# class Soluton5():
#     def searchRange(self, nums: [int], target: int) -> [int]:
#         ans = [-1, -1]
#         n = len(nums)
#         if n == 0:
#             return ans
#
#         left = 0
#         right = n - 1
#         while left < right:
#             mid = left + (left + right) // 2
#             if nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid
#         if nums[left] != target:
#             return ans
#
#         ans[0] = left
#
#         left = 0
#         right = n - 1
#         while left < right:
#             mid = left + (right - left + 1) // 2
#             if nums[mid] > target:
#                 right = mid - 1
#             else:
#                 left = mid
#
#         if nums[mid] == target:
#             ans[1] = left
#
#         return ans
#
# class Solution6():
#     def sortColors(self,nums:[int])->None:
#         left=0
#         right=len(nums)-1
#         index=0
#         while left<=right:
#             if index<left:
#                 index+=1
#             elif nums[index]==0:
#                 nums[index] , nums[left]=nums[left],nums[index]
#                 left+=1
#             elif nums[index]==2:
#                 nums[index],nums[right]=nums[right],nums[index]
#             else:
#                 index+=1
#
#
# class Solution7():
#     def insertsort(self, nums: [int]):
#         for i in range(1, len(nums)):
#             temp = nums[i]
#             j = i
#             while j > 0 and nums[j - 1] > temp:
#                 nums[j] = nums[j - 1]
#                 j -= 1
#             nums[j] = temp
#         return nums
#
#     def sortarry(self, nums: [int]) -> [int]:
#         return self.insertsort(nums)
#
# class Solution8():
#     def bubble(self, nums):
#
#         for i in range(len(nums) - 1):
#
#             for j in range(len(nums) - i - 1):
#
#                 if nums[j] > nums[j + 1]:
#                     nums[j], nums[j + 1] = nums[j + 1], nums[j]
#         return nums
#
#     def sortarry(self, nums: [int]) -> [int]:
#         return self.bubble(nums)
#
#
# ans = Solution8()
# list = [6, 2, 3, 5, 1, 4]
# print(ans.sortarry(list))
