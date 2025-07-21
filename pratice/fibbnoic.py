class Solution:
    def fib(self, n):
        #your code goes here
        if n==1:
            return 1
        elif n==0:
            return 0
        else:
            return self.fib(n-1)+self.fib(n-2)    
n =int(input("n"))
sol = Solution()
print(sol.fib(n))               