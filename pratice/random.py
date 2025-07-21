import random
n = random.randint(1,100)
count = 0
while True:
   u = int(input("enter the number"))
   count+=1
   if n==u:
      print("u gessed the right number")
   elif u>n:
      print("lower number")   
   elif u<n:
      print("higher number")   
 
   print(f"u have gussed the number in {count} attemts")       
     
      