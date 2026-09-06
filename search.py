import math

# Leetcode - Problem: 875

# Koko eating bananas
def findMinimumPilePerHour(piles, h):
    def find_hours(piles, banana_rate):
        # Find the hours to finish the piles if n bananas is eaten per hour
        res = 0
        for pile in piles:
            res += math.ceil(pile / banana_rate)

        return res

    low, high = 1, max(piles)
    while low <= high:
        mid = (low+high) // 2
        hours = find_hours(piles, mid)

        if hours > h:
            low = mid+1
        else:
            high = mid-1
    return low

# Leetcode - Problem: 33

def searchElementInRotated(nums, elem):
    low, high = 0, len(nums)-1

    while low <= high:
        mid = (low+high) // 2

        if elem > max(nums):
            return False

        if nums[mid] == elem:
            return True

        if nums[mid] >= nums[low]:
            # left half is sorted
            if nums[low] <= elem and elem <= nums[mid]:
                high = mid-1
            else:
                low = mid+1
        else:
            # right half is sorted
            if nums[mid] <= elem and elem <= nums[high]:
                low = mid+1
            else:
                high = mid-1
    return False


# Leetcode - Problem: 81

def searchElementInRotated2(nums, elem):
    low, high = 0, len(nums)-1

    while low <= high:
        mid = (low+high) // 2

        if elem > max(nums):
            return False

        if nums[mid] == elem:
            return True

        # trim search space if duplicate
        if nums[low] == nums[mid] and nums[mid] == nums[high]:
            low += 1
            high -= 1
            continue

        if nums[mid] >= nums[low]:
            # left half is sorted
            if nums[low] <= elem and elem <= nums[mid]:
                high = mid-1
            else:
                low = mid+1
        else:
            # right half is sorted
            if nums[mid] <= elem and elem <= nums[high]:
                low = mid+1
            else:
                high = mid-1
    return False

# Leetcode - Problem: 153

def minimumInRotatedSorted(nums):
    low, high = 0, len(nums)-1
    min_value = float("+inf")

    while low<=high:
        mid = (low+high) // 2

        if nums[mid] >= nums[low]:
            # left half is sorted
            min_value = min(min_value, nums[low])
            low = mid + 1
        else:
            # right half is sorted
            min_value = min(min_value, nums[mid])
            high = mid - 1
    return min_value


def numberOfTimesRotated(nums):
    min_value = float("+inf")
    low, high, times = 0, len(nums)-1, 0

    if nums[low] <= nums[high]:
        return 0

    while low <= high:
        mid = (low+high) // 2

        if nums[mid] >= nums[low]:
            # left half is sorted
            if nums[low] < min_value:
                times = low     # index of minimum is the times rotated
                min_value = nums[low]
            low = mid + 1
        else:
            # right half is sorted
            if nums[mid] < min_value:
                times = mid
                min_value = nums[mid]
            high = mid - 1
    return times


# Leetcode - Problem: 1482

def minimumDaysToMakeMBouquets(days, m, k):
    if (m*k) > len(days):
        return -1

    def check_possible(days, day, m, k):
        count, res = 0, 0

        for d in days:
            if d <= day:
                count += 1

                if count == k:
                    res += 1
                    count = 0
            else:
                count = 0

        return res >= m

    min_days = float("+inf")
    low, high = min(days), max(days)

    while low <= high:
        mid = (low+high) // 2
        is_possible = check_possible(days, mid, m, k)

        if is_possible:
            min_days = min(min_days, mid)
            high = mid - 1
        else:
            low = mid + 1

    return min_days
