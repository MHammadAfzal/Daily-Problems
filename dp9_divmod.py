# Read 2 integers a and b
# print 3 lines
#    - First line => a // b (Quotient)
#    - Second line => a % b (Remainder)
#    - Third line => (Quotient, Remainder)

"""
!START
? ----------- Input ----------
Enter first num: 187
Enter second num: 10
? ----------- Output ----------
Quotient: 18
Remainder: 7
Both: (18, 7)
!END
"""

"""
? -------> Pseudocode
-> Get first integer from user namely num1
-> Get second integer from user namely num2
-> Print quotient 
-> Print remainder 
-> Print quotient and remainder
"""


# Main function with all functionality
def main():
    num1 = int(input("What's first integer? "))
    num2 = int(input("What's second integer? "))
    print_all(num1, num2)


# Function to print quotient and remainder
def print_all(n1, n2):
    print("Quotient: {}".format((n1 // n2)))
    print("Remainder: {}".format((n1 % n2)))
    print("Divmod: {}".format((divmod(n1, n2))))


if __name__ == "__main__":
    main()
