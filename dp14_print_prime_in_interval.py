# Given an integer n
# Print prime numbers from a to b

"""
!START
? -------- Input -----------
First Num: 5
Second Num: 15
? -------- Output -----------
Prime Numbers from 5 to 10: 5 7 11 13
!END
"""


"""
? ------> Pseudocode
=> Get an integer from user namely a (Starting Point)
=> Get an integer from user namely b (Ending Point)
=> Call function to print prime numbers till b
    -> Start Loop
        - Loop from a to b
        - Call function to check prime number
            - if prime
                - print number
            - else 
                - Continue
    -> End Loop
"""


# check if a number is prime
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# print prime numbers
def print_prime_nums(num1, num2):
    for i in range(num1, num2):
        print(i, end=" ") if is_prime(i) else ...


# Main function having control of the program
def main():
    prime_start = int(input("Enter Starting Point: "))
    prime_end = int(input("Enter Ending Point: "))
    print("Prime Numbers from {} to {}".format(prime_start, prime_end))
    print_prime_nums(prime_start, prime_end)


# Driver's code
if __name__ == "__main__":
    main()
