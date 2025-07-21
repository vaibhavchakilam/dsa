class Solution:
    
    def isArmstrong(self, n):
        
       temp = n
       count =0
       while temp>0:
          temp = temp//10
          count = count+1

       temp =n
       sum =0
       while temp>0:
            digit = temp%10
            sum = sum + digit**count
            temp = temp//10

n =int(input("enter the n valye"))
if(sum == n):
        print("it is a amstronng number")    
else:
        print("it is not a amstrong number")    

sol =   Solution()
print(sol.isArmstrong(n))

