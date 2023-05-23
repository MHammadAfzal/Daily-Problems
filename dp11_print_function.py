#  Read an integer n
#  Print from 1 to n


"""
!START
? ----------- Input ----------
Enter an integer: 5
? ----------- Output ----------
Result: 12345
!END
"""

"""
? ------> Pseudocode
-> Get an integer from the user namely num
-> Initiate a loop till num:
    -> Print the number
"""


def print_numbers(n):
    for i in range(1, n + 1):
        print(i, end="")


# Main function with all functionality
def main():
    num = int(input("Enter an integer: "))
    print_numbers(num)


# Calling the main function
if __name__ == "__main__":
    main()
