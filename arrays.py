from typing import List

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
    return l+1


# Leetcode - Problem 11

"""You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

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
