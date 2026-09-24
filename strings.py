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

        if l < r and s[l].lower() != s[r].lower():
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

    column_width = (numRows * 2) - 2
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
                after = column_width - (2 * i)
                if after + j < len(s) and numRows - i > 1:
                    res += s[after + j]

            j += column_width  # calculation of the next constant column

    return res


# Leetcode - Problem: 187


def findRepeatedDnaSequences(s):
    """
    :type s: str
    :rtype: List[str]
    """

    left, res = 0, []
    sequences = defaultdict(int)

    for right in range(len(s)):
        if (right - left) + 1 < 10:
            continue

        sequence = s[left : right + 1]
        sequences[sequence] += 1

        if sequences[sequence] > 1 and sequence not in res:
            res.append(sequence)
        left += 1

    return res


# print(findRepeatedDnaSequences("AAAAACCCCC AAAAACCCCC CAAAAAGGGTTT"))
# print(findRepeatedDnaSequences("AAAAAAAAAAAAA"))
# print(findRepeatedDnaSequences("ACACACACACACACAC"))


# Z algorithm
def z_algorithm(s):
    l, r = 0, 0
    z_array = [0] * len(s)

    for i in range(1, len(s)):
        if i > r:
            # if i is outside the z-box
            l, r = i, i

            while r < len(s) and s[r - l] == s[r]:
                r += 1
            z_array[i] = r - l
            r -= 1
        else:
            k = i - l

            if z_array[k] < r - i + 1:
                z_array[i] = z_array[k]
            else:
                l = i

                while r < len(s) and s[r - l] == s[r]:
                    r += 1
                z_array[i] = r - l
                r -= 1
    return z_array


# leetcode - Problem: 1652


def findAnagrams(s, p):
    left, p_length, anag = 0, 0, []
    p_dict, p_freq = defaultdict(int), defaultdict(int)

    for k in p:
        p_length += 1
        p_dict[k] += 1

    for right in range(len(s)):
        curr_char = s[right]

        if curr_char not in p_dict:
            left = right + 1
            p_freq = defaultdict(int)
            continue

        if right - left + 1 > p_length:
            if s[left] in p_freq:
                p_freq[s[left]] -= 1
            left += 1

        if curr_char:
            p_freq[curr_char] += 1

        if right - left + 1 == p_length:
            is_anag = True
            for k, v in p_freq.items():
                is_anag = is_anag and p_dict[k] == v

            if is_anag:
                anag.append(left)
    return anag

# leetcode - Problem: 28

def strStr1(haystack: str, needle: str):
    concat_str = needle + "$" + haystack
    z_array = z_algorithm(concat_str)

    print(z_array)

    needle_length = len(needle)
    for i, v in enumerate(z_array):
        if needle_length == v:
            return i - (needle_length + 1)
    return -1
