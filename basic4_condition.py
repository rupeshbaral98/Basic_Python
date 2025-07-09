userName = input("Enter your name: ")
password = input("Enter your password: ")

if userName.lower() == "rupesh" and password.lower()== "1234":
    print("welcome ",userName)
elif userName == "admin" and password == "admin":
    print("Welcome ",userName)
else:
    print("Invalid credentials with UserName ",userName," & password ",password)


# This code checks the user credentials and prints a welcome message if the credentials are correct.
# If the credentials are incorrect, it prints an invalid credentials message with the provided username and password.
# The code uses `lower()` to ensure case-insensitive comparison for the username and password.


number=input("Enter a number: ") #always returns string
num = int(number) # convert string to integer
while(num < 10 and num >= 0):
    print(num)
    num -= 1
# This code prompts the user to enter a number and then enters a loop that continues as long as the number is less than 10.
# Inside the loop, it prints the current value of the number and increments it by 1.
# However, this code will raise an error because `number` is a string and cannot be compared with an integer.
# To fix this, you should convert `number` to an integer using `int(number)` before the comparison.

for x in range(1, 11): # range(start, end) -> end is exclusive
    if x % 2 == 0: # check if x is even
        print(x, "is even")
    else:
        print(x, "is odd")
# This code iterates through numbers from 1 to 10 and checks if each number is even or odd.
# It prints whether the number is even or odd based on the condition `x % 2 == 0`.

for x in userName:
    print(x, end =" ") #same line print