# Problem Statement
# Write a program to solve this age-related riddle!

# Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

# Anton is 21 years old.

# Beth is 6 years older than Anton.

# Chen is 20 years older than Beth.

# Drew is as old as Chen's age plus Anton's age.

# Ethan is the same age as Chen.

# Your code should store each person's age to a variable and print their names and ages at the end. The autograder is sensitive to capitalization and punctuation, be careful! Your solution should look like this (the below numbers are made up -- your solution should have the correct values!):

# Anton is 21
# Beth is 27
# Chen is 47
# Drew is 68
# Ethan is 47
def main():
    Anton =21
    Beth=Anton+6
    Chen=20+Beth
    Drew=Chen+Anton
    Ethan=Chen
    print(f"Anton is {Anton}")
    print(f"Beth is {Beth}")
    print(f"Chen is {Chen}")
    print(f"Drew is {Drew}")
    print(f"Ethan is {Ethan}")
main()