# Given an integer n
# Check if it is prime or not


"""
!START
? --------- Input -----------
7
8
? --------- Output -----------
7 is a prime number
7 is not a prime number
!END
"""

"""
? ------> Pseudocode
=> Get an integer from user namely n
=> Call function to check if n is prime?
    -> Start Loop
        -> Loop until n
        -> check if n is divisible by numbers from 2 to n-1
        -> if it is divisible 
            - return false
        -> else
            - pass
    -> End Loop
    -> return true
=> print that n is prime or not
"""


# check if a number is prime or not
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


#  Main function with all functionality
def main():
    n = int(input("Enter a number: "))
    print("{} is {} prime number".format(n, "a" if is_prime(n) else "not a"))


# Driver's code
if __name__ == "__main__":
    main()
