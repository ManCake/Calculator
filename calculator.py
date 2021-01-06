

def main():
    print("What type of operation?")
    print("(+) (-) (*) (/)")
    operator = input()

    if operator == "+":
        print("What 2 numbers do you want to add?")
        number_1 = int(input())
        number_2 = int(input())
        add(number_1, number_2)
        
def add(number_1, number_2):
    total = number_1 + number_2
    print("The sum is:", total)
    
def subtract (number_1, number_2):
    difference = number_1 - number_2
    print("the difference is:", difference)

def multiply(number_1, number_2): 
    product = number_1 * number_2
    print("The product is:", product)
    
# Program Flow
main()