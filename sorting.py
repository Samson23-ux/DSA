from typing import List


# Insertion sort
def insertion_sort(data: list[int]) -> list[int]:
    for i in range(1, len(data)):
        curr_elem = data[i]
        prev_index = i - 1

        while prev_index >= 0 and data[prev_index] > curr_elem:
            data[prev_index + 1] = data[prev_index]
            prev_index -= 1
        data[prev_index + 1] = curr_elem
    return data


def recursive_insertion_sort(data: list[int], i=None) -> list[int]:
    if i is None:
        i = 1

    if i < len(data):
        curr_elem = data[i]
        prev_index = i - 1

        while prev_index >= 0 and data[prev_index] > curr_elem:
            data[prev_index + 1] = data[prev_index]
            prev_index -= 1
        data[prev_index + 1] = curr_elem

        recursive_insertion_sort(data, i + 1)
    return data


# Selection sort
def selection_sort(data: list[int]) -> list[int]:
    for i in range(len(data) - 1):
        smallest_index = i
        j = i + 1

        while j < len(data):
            if data[smallest_index] > data[j]:
                smallest_index = j
            j += 1
        data[i], data[smallest_index] = data[smallest_index], data[i]
    return data


# Neetcode - Problem: 1630

"""Implement Insertion Sort and return intermediate states.

Insertion Sort is a simple sorting algorithm that builds the sorted list one element at a time, from left to right.
It works by repeatedly taking an element from the unsorted portion and inserting it into its correct position in the sorted portion of the list.

Objective:

Given a list of key-value pairs, sort the list by key using Insertion Sort.
Return a list of lists showing the state of the array after each insertion.
If two key-value pairs have the same key, maintain their relative order in the sorted list.

Input:

pairs - a list of key-value pairs, where each key-value has an integer key and a string value. (0 <= pairs.length <= 100)."""


# Difficulty - Easy

# solution


# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value


class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if len(pairs) == 0:
            return []
        res = [pairs[:]]
        for i in range(1, len(pairs)):
            curr_pair = pairs[i]
            curr_elem = curr_pair.key
            prev_index = i - 1

            while prev_index >= 0 and pairs[prev_index].key > curr_elem:
                pairs[prev_index + 1] = pairs[prev_index]
                prev_index -= 1
            pairs[prev_index + 1] = curr_pair
            res.append(pairs[:])
        return res


# Complexity

# Time complexity - O(n^2)
# Space complexity - O(n^2)

# Leetcode - Problem: 1630

"""A sequence of numbers is called arithmetic if it consists of at least two elements,
and the difference between every two consecutive elements is the same.
More formally, a sequence s is arithmetic if and only if s[i+1] - s[i] == s[1] - s[0] for all valid i.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic:

1, 1, 2, 5, 7
You are given an array of n integers, nums, and two arrays of m integers each, l and r, representing the m range queries,
where the ith query is the range [l[i], r[i]]. All the arrays are 0-indexed.

Return a list of boolean elements answer, where answer[i] is true if the subarray nums[l[i]], nums[l[i]+1], ... , nums[r[i]]
can be rearranged to form an arithmetic sequence, and false otherwise.
"""

# Solution

# Algorithm
# 1. Run a loop from i=0 to m-1
# 2. Get the subarray conrresponding to nums[l[i]:r[i]]
# 3. Sort the subarry
# 4. Run another loop from d=2 to length of subarray
# 5. Check if consecutive integers have the same difference


def checkArithmeticSubarrays(nums, l, r):
    """
    :type nums: List[int]
    :type l: List[int]
    :type r: List[int]
    :rtype: List[bool]
    """

    answer = []
    for i in range(len(l)):
        sub_array = nums[l[i] : r[i] + 1]
        sub_array.sort()

        is_arithmetic = True
        for d in range(2, len(sub_array)):
            is_con = (
                sub_array[d] - sub_array[d - 1] == sub_array[d - 1] - sub_array[d - 2]
            )
            is_arithmetic = is_arithmetic and is_con

        answer.append(is_arithmetic)
    return answer


# time complexity -> O(m*n(logn))
# space complexity -> O(n*m)

# Solution 2 of problem 1630 - Uisng sets and mathematical properties


def checkArithmeticSubarrays2(nums, l, r):
    """
    :type nums: List[int]
    :type l: List[int]
    :type r: List[int]
    :rtype: List[bool]
    """

    # using arithmetic sequence
    # t(n) = a + (n-1)d; where t(n) = last term

    """Since the elements are integers and the difference
    bewtween each consecutive numbers must be the same,
    the elements increase by the same amount (arithmetic sequence).
    
    First step is to calculate the common difference (d) by using
    the max and min elements of each subarray and their length.
    The min and max elements correspond to the first and last element
    in the sequence.
    
    Any element i from the subarray minus the min element must be divisible
    by the common difference to be a valid arithmetic sequence
    
    Edge cases:
    1. The subarray is a valid sequence if the length <= 2
    2. If the diff (max-min) == 0, the subarray contain the same elements
    and by definition of the problem (s[i+1] - s[i] == s[1] - s[0]), is a 
    valid sequence
    3. If the diff is not a factor of (n-1), then it is not a valid arithmetic
    sequence since all elements are integers
    4. Duplicate elements cannot produce a valid arithmetic sequence
    """

    answer, arr_mem = [], {}
    for i in range(len(l)):
        arr_mem, is_arithmetic = set(), False
        min_value, max_value = float("+inf"), float("-inf")

        sub_array = nums[l[i] : r[i] + 1]

        if len(sub_array) <= 2:
            is_arithmetic = True
        else:
            for j in range(len(sub_array)):
                min_value = min(min_value, sub_array[j])
                max_value = max(max_value, sub_array[j])

            diff = max_value - min_value
            common_diff = diff / (len(sub_array) - 1)
            is_int = diff % (len(sub_array) - 1) == 0

            if not is_int:
                answer.append(is_arithmetic)
                continue

            for d in range(len(sub_array)):
                arr_mem.add(sub_array[d])

                if min_value == max_value:
                    is_arithmetic = True
                    break
                elif ((sub_array[d] - min_value) % common_diff) == 0 and len(
                    arr_mem
                ) > d:
                    is_arithmetic = True
                else:
                    is_arithmetic = False
                    break

        answer.append(is_arithmetic)
    return answer


# merge sort algorithm
def merge(nums, p, q, r):
    n1, n2 = q - p + 1, r - q
    left, right = [], []

    for i in range(n1):
        left.append(nums[p + i])
    for j in range(n2):
        right.append(nums[q + 1 + j])

    left.append(float("+inf")), right.append(float("+inf"))

    i, j = 0, 0

    for k in range(p, r + 1):
        if left[i] <= right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1


def merge_sort(nums, p=0, r=None):
    if r is None:
        r = len(nums) - 1

    if p < r:
        q = (p + r) // 2

        merge_sort(nums, p, q)
        merge_sort(nums, q + 1, r)
        merge(nums, p, q, r)
    return nums


# Bubble sort
def bubble_sort(nums):
    for i in range(len(nums) - 1, 0, -1):
        is_swapped = False
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                is_swapped = True
        if not is_swapped:
            return nums
    return nums


def recursive_bubble_sort(nums, i=None):
    if i is None:
        i = len(nums) - 1

    if i > 0:
        is_swapped = False
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                is_swapped = True
        if not is_swapped:
            return nums

        recursive_bubble_sort(nums, i - 1)
    return nums


# Quick sort
def quick_sort(nums, start = 0, end = None):
    if end is None:
        end = len(nums) - 1

    def partition(nums, start, end):
        # pivot is chosen to be the last element
        l, r = start, end-1

        while l < r:
            if nums[l] <= nums[end]:
                l += 1
            elif nums[r] > nums[end]:
                r -= 1
            else:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        # check finally for the last element
        # return end if it is less than our pivot
        # i.e. the last element is in its right position
        if nums[l] < nums[end]:
            return end
        else:
            # swap the pivot and the last element
            # and return the index of the last element
            nums[l], nums[end] = nums[end], nums[l]
            return l

    if start < end:
        print(nums)
        print()
        partition_index = partition(nums, start, end)
        quick_sort(nums, start, partition_index-1)
        quick_sort(nums, partition_index+1, end)
    return nums


# Leetcode - Problem: 4011
def countRatioSubarrays(nums, a, b):
    """
    :type nums: List[int]
    :type a: int
    :type b: int
    :rtype: int
    """

    res = 0
    for i in range(len(nums)):
        x, y = 0, 0
        for j in range(i, len(nums)):
            if nums[j] % 2 == 0:
                x += 1
            else:
                y += 1
            
            if y > 0 and (x * b) <= (y * a):
                res += 1
    return res
print(countRatioSubarrays([2,2,2], 1, 1))
