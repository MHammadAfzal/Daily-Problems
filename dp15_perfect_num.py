# Given an integer n
# Find the divsors of n
# Find the sum of divisors of n
# Check sum is equal to n - If yes, then n is a perfect number
# Return the answer


"""
!START
? ------- Input ---------
n: 6
n: 15
? ------- Output ---------
6 is a perfect number
15 is not a perfect number
!END
"""

"""
? -------> Pseudocode
=> Get an integer from user namely check_perfect
=> Declare a variable divisor_sum equals 1
=> Call a function to find divisors and it's sum
    -> Start Loop from 2 to n(check_perfect)
        - check if n divides i equals zero
            - if yes -> add i, n/i to divsor_sum
            - otherwise do nothing
    return divsor_sum
=> Call a function to check that n(check_perfect) is perfect
    -> check n equals divisor_sum
            - if yes
                - return n is perfect
            - if no
                - return n is not perfect
=> Print the result that n is perfect or not
=> Done!!!
"""


def get_divisor_sum(num):
    sum = 1
    i = 2
    while i * i <= num:
        if num % i == 0:
            sum = sum + i + num / i
        i += 1
    return sum


def is_perfect(num, sum):
    return num == sum


# Main function having control of the program
def main():
    check_perfect = int(input("Enter the number to check: "))
    divisor_sum = get_divisor_sum(check_perfect)
    res = "a" if is_perfect(check_perfect, divisor_sum) else "not a"
    print("{} is {} perfect number".format(check_perfect, res))


# Driver's code
if __name__ == "__main__":
    main()
