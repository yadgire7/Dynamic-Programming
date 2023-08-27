'''

Problem: To find the sum of the first n natural numbers

Objective function:
f(i): The sum of the first i natural numbers

Recurrence relation:
f(i) = f(i-1) + i

'''

# Implementation

def nSum(n):
    dp = [0]*(n+1)
    dp[0] = 0
    for i in range(1, n+1):
        dp[i] = dp[i-1] + i
    return dp[n]


check = nSum(4)
print(check)