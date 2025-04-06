# Problem Statement
# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

# An example run of the program looks like this (user input is in blue):

# Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.
# solution
def get_user_num():
    user_num=[]
    
    while True:
        get_input=input("Enter a number: ")
        if get_input =="":
            break
        input_int=int(get_input)
        user_num.append(input_int)
    return user_num   
def count_num(num_lst):
    num_dict={}
    for nums in num_lst:
        if nums not in num_dict:
            num_dict[nums]=1
        else :
            num_dict[nums]+=1
    return num_dict 
def print_counts(num_dict):
        for num in num_dict:
            print(f"{num} appears {num_dict} times")

                   

def main():
    user_numbers=get_user_num()
    num_dic=count_num(user_numbers)
    print_counts(num_dic)
main()    


