 ## 1️⃣ 01_add_two_numbers 
# **Description:**  
# ## Problem Statement
# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

# Prompt the user to enter the first number.

# Read the input and convert it to an integer.

# Prompt the user to enter the second number.

# Read the input and convert it to an integer.

# Calculate the sum of the two numbers.

# Print the total sum with an appropriate message.

# The provided solution demonstrates a working implementation of this problem, where the main() function guides the user through the process of entering two numbers and displays their sum.  


def main():
    print("Calculate sum two numbers")
    num1=input("Enter the first number: ")
    num2=input("Enter the second number: ")
  
    
    sum=  int(num1)+ int(num2)
    print(num1, "+", num2 ,"=", sum )

main()