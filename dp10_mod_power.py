# Read 3 integers a, b, and m
# print 2 lines
#      - First Line -> a raise to the power b
#      - Second Line -> a raise to the power b mod m => ((a**b) % m)

"""
!START
? ----------- Input ----------
a: 3
b: 4
c: 5
? ----------- Output ----------
First line: 81
Second Line: 1
!END
"""

"""
? -------> Pseudocode
-> Get first integer from user namely num1
-> Get second integer from user namely num2
-> Get third integer from user namely num3
-> Calculate num1 raise to the power num2
-> Calculate num1 raise to the power num2 mod num3
-> Now print the values
"""


# Main function with all functionality
def main():
    num1, num2, num3 = get_values()
    print("First line:", pow(num1, num2))  # num1**num2
    print("Second line:", pow(num1, num2, num3))  # (num1**num2) % num3


# Function to get values from user
def get_values():
    n1 = int(input("Give us first integer: "))
    n2 = int(input("Give us second integer: "))
    n3 = int(input("Give us third integer: "))
    return n1, n2, n3


# Call main function
if __name__ == "__main__":
    main()
