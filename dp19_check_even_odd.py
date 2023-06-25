# Get number from user
# check if it is even or odd
# print the result


"""
!START
? ---------- Input -------------
num: 7, 2017
num: 4, 2022
? ---------- Output -------------
num: ODD
num: EVEN
!END
"""

"""
? -------------> Pseudocode
=> Get an integer from user namely num
=> Call a function to check if it is even or not
    -> Check if num is divided by 2
        - If Yes
            -- It is even
        - Else
            -- It is odd
    return true
=> Get true or false from function call
=> Print the result
"""


def is_even(num):
    return True if num % 2 == 0 else False


def main():
    num = int(input("What's num? "))
    res = is_even(num)
    print("{} is an {} number.".format(num, ("even" if res else "odd")))


if __name__ == "__main__":
    main()
