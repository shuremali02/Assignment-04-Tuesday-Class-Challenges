# Problem Statement
# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.
# solution
def get_first_elem(lst):
    print(lst[-1])
def get_lst():
    lst:list=[]
    prompt=input("Please enter an element of the list or press enter to stop. ")
    while prompt != "":
        lst.append(prompt)
        prompt=input("Please enter an element of the list or press enter to stop. ")
    return lst        
def main():
    my_list=get_lst()
    get_first_elem(my_list)
main()