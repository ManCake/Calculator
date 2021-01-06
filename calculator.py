#!/usr/bin

def main():
    print("What type of operation?")
    print("(+) (-) (*) (/)")
    operator = input()

    if operator == "+":
        print("What 2 numbers do you want to add?")
        number_1 = int(input())
        number_2 = int(input())
        add(number_1, number_2)
    
    elif operator == "-":
        print("What 2 numbers do you want to subtract?")
        number_1 = int(input())
        number_2 = int(input())
        subtract(number_1, number_2)

   elif operator == "*":
        print("What 2 numbers do you want to multiply?")
        number_1 = int(input())
        number_2 = int(input())
        multiply(number_1, number_2)

def add(number_1, number_2):
    total = number_1 + number_2
    print("The sum is:", total)
 
def subtract(number_1, number_2):
    difference = number_1 - number_2
    print("The difference is:", difference)


# Program Flow
main()
