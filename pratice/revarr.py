class Solution:
    def reverse(self, arr, n):

       i=1
       while i<=n:
         val =int(input("enter the val value"))
         arr.append(val)
         i+=1
       arr.reverse()
       print(arr)
n =int(input("enter the n value"))
arr = []       
sol = Solution()      
sol.reverse(arr,n)  


