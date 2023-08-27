'''
Problem: Climbing stairs
Given: size of staircase = n
Constraint: You can move up by either 1 step or 2 steps only
To find: Number of ways in which you can climb the staircase
'''

'''
Steps to follow to solve a DP problem:
1. Define the objective function:
    F(i) is the number of ways to go to the ith step
2. identify the base cases
    F(0) = 1
    F(1) = 1
    F(2) = 2
    F(3) = 3
    F(4) = 5
3. write a recurrence relation for optimized objective function
    F(n) = F(n-1) + F(n-2)
4. find order of execution
    bottom up
5. find where to look for the answer
'''

def climbStairs(n):
    # create a list for number of steps
    dp = [0]* (n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]   
    return dp[n]


test = climbStairs(5)
print(test)