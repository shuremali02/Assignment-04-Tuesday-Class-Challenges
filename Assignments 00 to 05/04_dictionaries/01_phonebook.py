# Problem Statement
# In this program we show an example of using dictionaries to keep track of information in a phonebook.
# solution
def phone_data():
    phonebook={}
    
    while True:
        get_name=input("Name: ")
        if get_name =="":
            break
        get_num=input("Number: ")
        phonebook[get_name]=get_num
    return phonebook
def display_data(phonebook):
    for name in phonebook:
        print(f"{name} -> {phonebook[name]}")

def lookup_numb(phonebook):
    while True:
        private_name=input("Enter name to lookup: ")
        if private_name =="":
            break
        if private_name not in phonebook:
            print(f"{private_name} is not in the phonebook")        
        else:
            print(phonebook[private_name])    

def main():
    phonebook=phone_data()
    display_data(phonebook)
    lookup_numb(phonebook)
main()