# Problem Statement
# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.
# solution

def main():
    feet:float=float(input("\nEnter number of feet: "))
    inches:float= feet * 12
    print(f"Your Feet {feet} in Inches {inches}")
main()    