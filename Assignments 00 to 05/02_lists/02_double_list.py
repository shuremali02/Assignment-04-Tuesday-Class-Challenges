# Problem Statement
# Write a program that doubles each element in a list of numbers. For example, if you start with this list:

# numbers = [1, 2, 3, 4]

# You should end with this list:

# numbers = [2, 4, 6, 8]

def add_numbers(numbers):
    total_so_far:list[int]=[]
    for i in numbers:
        i+=i
        total_so_far.append(i)
  
    return total_so_far
def main():
    numbers:list[int]=[1,2,3,4,5,6]
    sum_of_numbers=add_numbers(numbers)
    print(sum_of_numbers)
main()    
    
