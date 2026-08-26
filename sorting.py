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


# Neetcode - Problem:

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
        if len(pairs) == 0: return []
        res = [pairs[:]]
        for i in range(1, len(pairs)):
            curr_pair = pairs[i]
            curr_elem = curr_pair.key
            prev_index = i-1

            while prev_index >= 0 and pairs[prev_index].key > curr_elem:
                pairs[prev_index+1] = pairs[prev_index]
                prev_index -= 1
            pairs[prev_index+1] = curr_pair
            res.append(pairs[:])
        return res

# Complexity 

# Time complexity - O(n^2)
# Space complexity - O(n^2)

# Leetcode - Problem: 1630

"""A sequence of numbers is called arithmetic if it consists of at least two elements, and the difference between every two consecutive elements is the same.
More formally, a sequence s is arithmetic if and only if s[i+1] - s[i] == s[1] - s[0] for all valid i.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic:

1, 1, 2, 5, 7
You are given an array of n integers, nums, and two arrays of m integers each, l and r, representing the m range queries, where the ith query is the range [l[i], r[i]]. All the arrays are 0-indexed.

Return a list of boolean elements answer, where answer[i] is true if the subarray nums[l[i]], nums[l[i]+1], ... , nums[r[i]] can be rearranged to form an arithmetic sequence, and false otherwise.
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
        sub_array = nums[l[i]:r[i]+1]
        sub_array.sort()

        is_arithmetic = True
        for d in range(2, len(sub_array)):
            is_con = sub_array[d] - sub_array[d-1] == sub_array[d-1] - sub_array[d-2]
            is_arithmetic = is_arithmetic and is_con

        answer.append(is_arithmetic)
    return answer

# time complexity -> O(m*n(logn))
# space complexity -> O(n*m)
