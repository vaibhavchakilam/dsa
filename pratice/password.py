import random
char = "1234567890!@#$%^&*()_+qwertyuiop[]';lkjhgfdaazxcvbnm,./"
length =  int(input("enter the len"))
password =""

for i in range(length):
    password +=random.choice(char)
print(password)    
    