class Solution:

    def countDigit(self, n):

        if n == 0:

            return 1

            

        count =0    

        while n>0:

            n//=10    

            count+=1

        return count 



sol = Solution()       



print(sol.countDigit(123))