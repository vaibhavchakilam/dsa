class Solution:
    def NnumbersSum(self, N):
        #your code goes here
        Sum =0
        for i in range(1,N+1,1):
            print(i)
            Sum = Sum+i
        print(Sum)    
N =int(input("Enter the n value"))        
sol = Solution()
sol.NnumbersSum(N)
