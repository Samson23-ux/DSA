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
