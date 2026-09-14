from typing import List
from collections import Counter

# Leetcode - Problem 1

# Two Sum

def twoSum(nums: List[int], target: int) -> List[int]:
    hash_table = {}
    for index, value in enumerate(nums):
        res = target - value
        if res in hash_table:
            return [hash_table[res], index]
        hash_table[value] = index


# Leetcode - Problem 27

def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """

    l, r = 0, len(nums) - 1
    len_val = 0
    while l <= r:
        while nums[r] == val and r >= 0:
            len_val += 1
            r -= 1
        if nums[l] == val and l < r:
            len_val += 1
            nums[l], nums[r] = nums[r], nums[l]
            r -= 1
        l += 1
    return len(nums) - len_val


# Leetcode - Problem 26

"""Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted."""


def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l = 0

    for r in range(1, len(nums)):
        if nums[l] != nums[r]:
            l += 1
            nums[l], nums[r] = nums[r], nums[l]
    return l + 1


# Leetcode - Problem 11

"""You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container."""


def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """

    l, r = 0, len(height) - 1

    max_amount = float("-inf")
    while l < r:
        a = r - l

        if height[l] <= height[r]:
            b = height[l]
            l += 1
        else:
            b = height[r]
            r -= 1
        max_amount = max(max_amount, a * b)
    return max_amount


# Leetcode - Problem 49

"""Given an array of strings strs, group the anagrams together. You can return the answer in any order.
 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other."""


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    words, res = {}, []

    for word in strs:
        sorted_word = sorted(word)

        if tuple(sorted_word) in words:
            word_group = words[tuple(sorted_word)]
            res[word_group].append(word)
        else:
            words[tuple(sorted_word)] = len(res)
            res.append([word])
    return res


# Leetcode - Problem 169

"""Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array."""

# Solution using 0(n) space


def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    count_rec = {}
    candidate = None
    max_count = float("-inf")

    for num in nums:
        if num not in count_rec:
            count_rec[num] = 0
        else:
            count_rec[num] += 1

        if count_rec[num] > max_count:
            max_count = count_rec[num]
            candidate = num
    return candidate


# Optimized solution using 0(1) space
# Boyer-Moore Majority Vote Algorithm


def majorityElementOptimized(nums):
    ### The input is generated such that a majority element will exist in the array.
    """
    :type nums: List[int]
    :rtype: int
    """

    candidate, count = None, 0
    for num in nums:
        if count == 0:
            candidate = num
            count += 1
        elif candidate == num:
            count += 1
        else:
            count -= 1

    ### Additional check for actual count if no strict
    ### majority is guaranteed to be present

    # actual_count = sum(1 for num in nums if num == candidate)

    # if actual_count > len(nums) // 2:
    #     return candidate
    # else:
    #     return None

    return candidate


# Leetcode - Problem 53

"Given an integer array nums, find the subarray with the largest sum, and return its sum"


def maxSubArray(nums):
    # kadane's Algorithm
    """
    :type nums: List[int]
    :rtype: int
    """

    max_sum = nums[0]
    current_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    return max_sum


def row_exists(row_group, row, val):
    if row not in row_group:
        row_group[row] = {val}
    else:
        if val in row_group[row]:
            return True
        row_group[row].add(val)
    return False

def col_exists(col_group, col, val):
    if col not in col_group:
        col_group[col] = {val}
    else:
        if val in col_group[col]:
            return True
        col_group[col].add(val)
    return False


def box_exists(box_group, box, val):
    if box not in box_group:
        box_group[box] = {val}
    else:
        if val in box_group[box]:
            return True
        box_group[box].add(val)
    return False


# Leetcode - Problem: 36

def validSoduko(soduko: list[list]):
    row_group = {}
    col_group = {}
    box_group = {}

    for row in range(len(soduko)):
        for col in range(len(soduko[row])):
            val = soduko[row][col]

            if val == ".":
                continue

            val = int(val)
            box = (row // 3) * 3 + (col // 3)

            if row_exists(row_group, row, val):
                return False
            if col_exists(col_group, col, val):
                return False
            if box_exists(box_group, box, val):
                return False
    return True

# Leetcode - Problem: 347

def kFrequentElement(nums, k):
    n = len(nums)
    counter = Counter(nums)
    bucket = [0] * (n+1)

    for key, freq in counter.items():
        if bucket[freq] == 0:
            bucket[freq] = [key]
        else:
            bucket[freq].append(key)

    res = []
    for i in range(n, -1, -1):
        if bucket[i] != 0:
            res.extend(bucket[i])
        if len(res) == k:
            break

    return res


# Leetcode - Problem: 

def trappingRainWater(nums):
    l, r = 0, len(nums)-1
    max_left, max_right = float("-inf"), float("-inf")

    total = 0

    while l < r:
        if nums[l] <= nums[r]:
            # process left before right
            if nums[l] < max_left:
                # maxleft is definately smaller than maxright
                # since we must have processed maxright first
                # if maxleft were to be greater
                total += max_left - nums[l]
            else:
                # our current is greater than maxleft so far
                max_left = nums[l]
            l += 1
        else:
            # process right before left
            if nums[r] < max_right:
                # maxright is definately smaller than maxleft
                # since we must have processed maxleft first
                # if maxright were to be greater
                total += max_right - nums[r]
            else:
                # our current is greater than maxright so far
                max_right = nums[r]
            r -= 1
    return total

# Leetcode - Problem: 

def buyAndSellStock(stocks):
    max_profit = 0
    min_price = float("inf")

    for stock in stocks:
        if stock <= min_price:
            min_price = stock
        else:
            res = stock - min_price
            max_profit = max(max_profit, res)
    return max_profit


# Leetcode - Problem: 66

def plusOne(digits):
    carry = 0
    for i in range(len(digits)-1, -1, -1):
        res = digits[i] + carry
        if i == len(digits)-1:
            res += 1

        if res > 9:
            res, carry = 10 % res, 10 // res
        else:
            carry = 0

        digits[i] = res

        if carry == 0:
            break

    if carry > 0:
        digits.insert(0, carry)
    return digits


# Leetcode - Problem: 13

def threeSum(nums):
    nums.sort()
    res, processed = [], set()

    for i in range(len(nums)-1):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        j, k = i+1, len(nums)-1
        while j < k:
            sum = nums[i] + nums[j] + nums[k]

            if sum == 0:
                if (nums[i], nums[j], nums[k]) not in processed:
                    res.append([nums[i], nums[j], nums[k]])
                    processed.add((nums[i], nums[j], nums[k]))

                j += 1
                k -= 1
            elif sum > 0:
                k -= 1
                while k < j and nums[k] == nums[k+1]:
                    k -= 1
            else:
                j += 1
                while k < j and nums[j] == nums[j-1]:
                    j += 1
    return res


# Leetcode - Problem: 16

def threeSumClosest(nums, target):
    nums.sort()
    closest = float("+inf")

    for i in range(len(nums)-1):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        j, k = i+1, len(nums)-1
        while j < k:
            sum = nums[i] + nums[j] + nums[k]

            if sum == target:
                return sum

            if abs(target-sum) < abs(target-closest):
                closest = sum

            if sum <= target:
                j += 1
                while k < j and nums[j] == nums[j-1]:
                    j += 1
            else:
                k -= 1
                while k < j and nums[k] == nums[k+1]:
                    k -= 1
    return closest
