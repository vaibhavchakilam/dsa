class Solution:
    def printNumbers(self, n):
        # Your code goes here
        for i in range (1,n+1):
         print(i)

n =int(input("enter the n value"))  
sol = Solution()
print(sol.printNumbers(n))      
