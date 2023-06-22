# Given 2 integers a and b
# Output the greater number

"""
!START
? ---------- Input -------------
a: +5, b: +7
a: -1, b: -8
? ---------- Output -------------
max: +7
max: -1
!END
"""

"""
? -------------> Pseudocode
=> Get an integer from user namely num1
=> Get another integer from user namely num2
=> Call a function to check max of 2 nums and pass as arguments
    -> Check if num1 is greater than num2
        - If yes -> return num1
        - Else   -> Return num2
=> Print whichever the number is returned
"""


def get_max(a, b):
    return (a, b) if a >= b else (b, a)


def main():
    num1 = int(input("What's first number? "))
    num2 = int(input("What's second number? "))
    max_num, min_num = get_max(num1, num2)
    print("{} is greater than {}".format(max_num, min_num))
    # max_num = max(num1, num2)
    # print("{} is greater".format(max_num))


if __name__ == "__main__":
    main()
