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
#
# class Solution9():
#     def selectsort(self, arr):
#         for i in range(len(arr) - 1):
#             min_i = i
#             for j in range(i + 1, len(arr)):
#                 if arr[j] < arr[min_i]:
#                     min_i = j
#             if i != min_i:
#                 arr[i], arr[min_i] = arr[min_i], arr[i]
#         return arr
#
#     def sortArry(self, nums: [int]) -> [int]:
#         return self.selectsort(nums)
#
#
# ans = Solution9()
# list = [6, 2, 3, 5, 1, 4]
# print(ans.sortArry(list))
#
# class Solution9():
#     def shellsort(self, arr):
#         size = len(arr)
#         gap = size // 2
#
#         while gap > 0:
#             for i in range(gap, size):
#                 temp = arr[i]
#                 j = i
#
#                 while j >= gap and arr[j - gap] > temp:
#                     arr[j] = arr[j - gap]
#                     j -= gap
#
#                 arr[j] = temp
#             gap = gap // 2
#         return arr
#
#     def sortArry(self, nums: [int]) -> [int]:
#         return self.shellsort(nums)
#
#
# ans = Solution9()
# list = [7, 2, 6, 8, 0, 4, 1, 5, 9, 3]
# print(ans.sortArry(list))
#
# class Solution10:
#     def merge(self, left_arr, right_arr):
#         arr = []
#         left_i = 0
#         right_i = 0
#         while left_i < len(left_arr) and right_i < len(right_arr):
#             if left_arr[left_i] < right_arr[right_i]:
#                 arr.append(left_arr[left_i])
#                 left_i += 1
#             else:
#                 arr.append(right_arr[right_i])
#                 right_i += 1
#
#         while left_i < len(left_arr):
#             arr.append(left_arr[left_i])
#             left_i += 1
#
#         while right_i < len(right_arr):
#             arr.append(right_arr[right_i])
#             right_i += 1
#         return arr
#
#     def mergeSort(self, arr):
#         if len(arr) <= 1:
#             return arr
#         mid = len(arr) // 2
#         left_arr = self.mergeSort(arr[0:mid])
#         right_arr = self.mergeSort(arr[mid:])
#         return self.merge(left_arr, right_arr)
#
#     def sortArry(self, nums: [int]) -> [int]:
#         return self.mergeSort(nums)
#
#
# list = [6, 2, 1, 3, 7, 5, 4, 8]
# ans = Solution10()
# print(ans.sortArry(list))
#
# import random
# class Solution11:
#     def randomPartition(self, arr: [int], low: int, high: int):
#         i = random.randint(low, high)
#         arr[i], arr[low] = arr[low], arr[i]
#         return self.partiton(arr, low, high)
#
#     def partition(self, arr: [int], low: int, high: int):
#         pivot = arr[low]
#         i = low + 1
#
#         for j in range(i, high + 1):
#             if pivot > arr[j]:
#                 arr[j], arr[i] = arr[i], arr[j]
#                 i += 1
#         arr[i - 1], arr[low] = arr[low], arr[i - 1]
#         return i - 1
#
#     def quickSort(self, arr, low, high):
#         if low < high:
#             pi = self.randomPartition(arr, low, high)
#             self.quickSort(arr, low, pi - 1)
#             self.quickSort(arr, pi + 1, high)
#
#         return arr
#
#     def sortArry(self, nums: [int]) -> [int]:
#         return self.quickSort(nums, 0, len(nums) - 1)

# class Solution12:
#     def twoSum(self, nums: [int], target: int) -> [int]:
#         for i in range(len(nums)):
#             left, right = i + 1, len(nums) - 1
#             while left < right:
#                 mid = left + (right - left) // 2
#                 if nums[i] + nums[mid] > target:
#                     right = mid
#                 else:
#                     left = mid + 1
#             if nums[left] + nums[i] == target:
#                 return [i + 1, left + 1]
#         return [-1, -1]

# class Solution13:
#     def twoSum(self, nums: [int], target: int) -> [int]:
#         left = 0
#         right = len(nums) - 1
#         while left < right:
#             if nums[left] + nums[right] == target:
#                 return [left + 1, right + 1]
#             elif nums[left] + nums[right] > target:
#                 right -= 1
#             else:
#                 left += 1
#         return [-1, -1]

# class Solution14:
#     def findMin(self,nums:[int])->int:
#         left=0
#         right=len(nums)
#         while left<right:
#             mid=left+(right-left)//2
#             if nums[mid]>nums[right]:
#                 left=right+1
#             else:
#                 right=mid
#         return nums[left]
#

# class Solution15:
#     def findMin(self, nums: [int]) -> int:
#         left = 0
#         right = len(nums)
#         while left < right:
#             mid = left + (right - left) // 2
#             if nums[mid] > nums[right]:
#                 left = mid + 1
#             elif nums[mid] < nums[right]:
#                 right = mid
#             else:
#                 right = right - 1
#         return nums[left]

# class Soluthion16:
#     def isPalindrome(self,s:str)->bool:
#         left=0
#         right=len(s)
#         while left<right:
#             if s[left].isalnum():
#                 left+=1
#                 continue
#             if s[right].isalnum():
#                 right+=1
#                 continue
#             if s[left].lower()==s[right].lower():
#                 left+=1
#                 right-=1
#             else:
#                 return  False
#         return True

# class Solution17:
#     def maxArea(self, height: [int]) -> int:
#         left = 0
#         right = len(height) - 1
#         ans = 0
#         while left < right:
#             area = min(height[left], height[right]) * (right - left)
#             ans = max(ans, area)
#             if height[left] < height[right]:
#                 left += 1
#             else:
#                 right -= 1
#         return ans

# class Solution18:
#     #快慢指针
#     def removeDuplicates(self, nums: [int]) -> int:
#         if len(nums) <= 1:
#             return nums
#
#         slow, fast = 0, 1
#
#         while (fast < len(nums)):
#             if nums[slow] != nums[fast]:
#                 slow += 1
#                 nums[slow] = nums[fast]
#             fast += 1
#         return slow + 1

# class Solution19:
#     def insertsection(self,nums1:[int],nums2:[int])->[int]:
#         nums1.sort()
#         nums2.sort()
#
#         left_1=0
#         left_2=0
#         res=[]
#         while left_1<len(nums1) and left_2<len(nums2):
#             if nums1[left_1]==nums2[left_2]:
#                 if nums1[left_1] not in res:
#                     res.append(nums1[left_1])
#                     left_1+=1
#                     left_2+=2
#             elif nums1[left_1]<nums2[left_2]:
#                 left_1+=1
#             elif nums1[left_1]>nums2[left_2]:
#                 left_2+=1
#         return res

# class Solution20:
#     def reverseSring(self, s: [str]) -> [str]:
#         left, right = 0, len(s) - 1
#         while left < right:
#             s[left], s[right] = s[right], s[left]
#             left += 1
#             right += 1

# class Solution21:
#     def reverseVowels(self, s: str) -> str:
#         vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#         left = 0
#         right = len(s) - 1
#         s_list = list(s)
#         while left < right:
#             if s_list[left] not in vowels:
#                 left += 1
#                 continue
#             if s_list[right] not in vowels:
#                 right += 1
#                 continue
#             s_list[left], s_list[right] = s_list[right], s_list[left]
#             left += 1
#             right += 1
#         return ''.join(s_list)

# class Solution22:
#     def triangleNember(self, nums: [int]) -> int:
#         nums.sort()
#         size = len(nums)
#         ans = 0
#
#         for i in range(2, size):
#             left = 0
#             right = i - 1
#             while left < right:
#                 if nums[left] + nums[right] <= nums[i]:
#                     left += 1
#                 else:
#                     ans += (right - left)
#                     right -= 1
#         return ans

# class Solution23:
#     def numOfSubarrays(self, arr: [int], k: int, threshold: int) -> int:
#         left = 0
#         right = 0
#         ans = 0
#         window_sum = 0
#
#         while right < len(arr):
#             window_sum += arr[right]
#
#             if right - left + 1 >= k:
#                 if window_sum >= k * threshold:
#                     ans += 1
#                 window_sum -= arr[left]
#                 left += 1
#             right += 1
#         return ans

# class Solution24:
#     def lengthOfLongestSubsting(self, s: str) -> int:
#         left = 0
#         right = 0
#         windows = dict()
#         ans = 0
#
#         while right < len(s):
#             if s[right] not in windows:
#                 windows[s[right]] = 1
#             else:
#                 windows[s[right]] += 1
#
#             while windows[s[right]] > 1:
#                 windows[s[left]] -= 1
#                 left += 1
#
#             ans = max(ans, right - left + 1)
#             right += 1
#
#         return ans

# class Solution25:
#     def minSubArryLen(self, target: int, nums: [int]) -> int:
#         size = len(nums)
#         ans = size + 1
#         left = 0
#         right = 0
#         window_sum = 0
#
#         while right < size:
#             window_sum += nums[right]
#
#             while window_sum >= target:
#                 ans = max(ans, right - left + 1)
#                 window_sum -= nums[left]
#                 left += 1
#             right += 1
#
#         return ans if ans != size + 1 else 0

# class Solution26:
#     def numSubarrayProductLessTank(self, nums: [int], k: int) -> int:
#         if k <= 1:
#             return 0
#         left = 0
#         right = 0
#         windows_product = 1
#         count = 0
#
#         while right < len(nums):
#             windows_product *= nums[right]
#
#             if windows_product >= k:
#                 windows_product /= nums[left]
#                 left += 1
#
#             count += (right - left + 1)
#             # 这里是因为每当right右移找到了一个新的满足条件的数组，新加入的nums[right]与前面的
#             #数的组合个数为right - left + 1,并且一定不会重复，因为nums[right]是第一次出现
#             right += 1
#         return count

# class Solution27:
#     def fingMaxAverage(self, nums: [int], k: int) -> float:
#         left = 0
#         right = 0
#         window_total = 0
#         ans = float('-inf')
#         while right < len(nums):
#             window_total += nums[right]
#             if right - left + 1 >= k:
#                 ans = max(window_total / k, ans)
#                 window_total -= nums[left]
#                 left += 1
#             right += 1
#
#         return ans

# class Solution28:
#     def maxSatisfied(self, customer: [int], grumy: [int], minutes: int) -> int:
#         left = 0
#         right = 0
#         window_count = 0
#         ans = 0
#
#         while right < len(customer):
#             if grumy[right] == 1:
#                 window_count += customer[right]
#
#             if right - left + 1 >= minutes:
#                 if grumy[left] == 1:
#                     window_count -= customer[left]
#                     left += 1
#
#             right += 1
#             ans = max(ans, window_count)
#
#         for i in range(len(customer)):
#             if grumy[i] == 0:
#                 ans += customer[i]
#
#         return ans

# class Solution29:
#     def maxVowels(self, s: str, k: int) -> int:
#         left = 0
#         right = 0
#         ans = 0
#         window_count = 0
#         vowels_set = ('a', 'e', 'i', 'o', 'u')
#
#         while right < len(s):
#             if s[right] in vowels_set:
#                 window_count += 1
#
#             if right - left + 1 >= k:
#                 ans = max(ans, window_count)
#                 if s[left] in vowels_set:
#                     window_count -= 1
#                 left -= 1
#
#             right += 1
#
#         return ans

from time import time, localtime, sleep


class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def main():
    # 通过类方法创建对象并获取系统时间
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()
