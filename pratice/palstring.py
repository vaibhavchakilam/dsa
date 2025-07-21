class Solution:    
    def palindromeCheck(self, s):
        #your code goes here
       
        if  s == s[::-1]:
            print("it is a pallendrome string")
        else:
             print("it is not pallendrome string")   
       
s =str(input("value of s is"))
  
sol =  Solution()
sol.palindromeCheck(s)     