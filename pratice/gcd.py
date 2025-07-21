class Solution:
    def GCD(self, n1, n2):
        if n2==0:
            return n1
        else:
            return (n2,n1%n2)
sol = Solution()
print(sol.GCD( 9, 8))             
