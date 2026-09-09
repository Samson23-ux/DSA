# Leetcode - Problem: 509

# Memoization
def fibonacciM(n):
    dp = [-1] * (n+1)

    def cal(n):
        if n == 0:
            dp[n] = 0
            return 0
        if n == 1:
            dp[n] = 1
            return 1

        if dp[n] != -1:
            return dp[n]

        res = cal(n-1) + cal(n-2)
        dp[n] = res
        return res

    return cal(n)


# Tabular
def fibonacciT(n):
    dp = [-1] * (n+1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# Leetcode - Problem: 

def climbStairsM(nums):
    dp = [-1] * (len(nums)+1)
    def cal(idx):
        if idx == 0 or idx == 1:
            return 1

        if dp[idx] != -1:
            return dp[idx]
        
        one_step = climbStairsM(idx-1)
        two_steps = climbStairsM(idx-2)
        
        res = one_step + two_steps
        dp[idx] = res
        return res

    return cal(len(nums)-1)

def climbStairsT(n):
    dp = [-1] * (n+1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n+1):
        one_step = dp[i-1]
        two_steps = dp[i-2]

        dp[i] = one_step + two_steps

    return dp[n]

# Leetcode - Problem: 198

def houseRobberM(nums):
    dp = [-1] * (len(nums)+1)

    def cal(idx):
        if idx == 0:
            return nums[idx]
        elif idx < 0:
            return 0

        if dp[idx] != -1:
            return dp[idx]

        pick = nums[idx] + cal(idx-2, nums)
        n_pick = 0 + cal(idx-1, nums)

        res = max(pick, n_pick)
        dp[idx] = res
        return res

    return cal(len(nums)-1)

# Tabular

def houseRobberT(nums):
    dp = [-1] * (len(nums)+1)
    dp[0] = nums[0]

    for idx in range(1, len(nums)):
        pick = nums[idx]
        if idx > 1:
            pick += dp[idx-2]

        n_pick = 0 + dp[idx-1]
        dp[idx] = max(pick, n_pick)

    return dp[len(nums)-1]


# Leetcode - Problem: 322

def coinChangeM(nums, target):
    dp =[[-1] * (target+1) for _ in range(len(nums))]
    def cal(idx, target, nums):
        if idx == 0:
            if target % nums[idx] == 0:
                return target // nums[idx]
            else:
                return -1

        pick = float("inf")
        if nums[idx] <= target:
            pick = 1 + cal(idx, target-nums[idx], nums)

        n_pick = 0 + cal(idx-1, target, nums)

        res = min(pick, n_pick)
        dp[idx][target] = res
        return res

    return cal(len(nums)-1, target, nums)


def coinChangeT(nums, target):
    dp =[[-1] * (target+1) for _ in range(len(nums))]

    for t in range(target+1):
        if t % nums[0] == 0:
            dp[0][t] = t // nums[0]
        else:
            dp[0][t] = 1e9

    for idx in range(1, len(nums)):
        for t in range(target+1):
            pick = float("inf")
            if nums[idx] <= t:
                pick = 1 + dp[idx][t-nums[idx]]

            n_pick = 0 + dp[idx-1][t]
            dp[idx][t] = min(pick, n_pick)

    return dp[len(nums)-1][target]
