from collections import defaultdict

# Leetcode - Problem 125

"""A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters,it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise."""

def isPalindrome(s: str):
    """
    :type s: str
    :rtype: bool
    """

    length = len(s)
    l, r = 0, length - 1

    while l < r:
        while l < length:
            if not s[l].isalnum():
                l += 1
            else:
                break
        while r >= 0:
            if not s[r].isalnum():
                r -= 1
            else:
                break

        if l < r:
            if s[l].lower() != s[r].lower():
                return False

        l += 1
        r -= 1
    return True

# Leetcode - Problem 387
"""Given a string s, find the first non-repeating character in it and return its index.
If it does not exist, return -1."""

def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """

    appearance = defaultdict(int)

    for w in s:
        appearance[w] += 1

    for index, value in enumerate(s):
        if appearance[value] == 1:
            return index
    return -1


# Leetcode - Problem 14

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """

    res = ""
    strs.sort()

    for i in range(len(strs[0])):
        if strs[0][i] != strs[-1][i]:
            break
        res += strs[0][i]
    return res


# Leetcode - Problem 6

def convert(s, numRows):
    res = ""

    column_width = (numRows*2) - 2
    if len(s) < numRows or numRows <= 1:
        return s

    for i in range(numRows):
        j = i

        while j < len(s):
            if i <= 0:
                res += s[j]
            else:
                res += s[j]

                # copy characters between the constant columns
                # the index of after decreases as the value of i(row) increases
                after = column_width - (2*i)
                if after+j < len(s) and numRows-i > 1:
                    res += s[after+j]

            j += column_width  # calculation of the next constant column

    return res
