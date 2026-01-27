class Solution:
    def climbStairs(n):
        if n <= 2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)