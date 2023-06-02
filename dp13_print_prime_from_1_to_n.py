# Given an integer n
# Print prime numbers from 1 to n

"""
!START
? -------- Input -----------
10
30
? -------- Output -----------
Prime Numbers from 1 to 10: 2 3 5 7
Prime Numbers from 1 to 30: 2 3 5 7 11 13 17 23 29
!END
"""


"""
? ------> Pseudocode
=> Get an integer from user namely n
=> Call function to print prime numbers till n
    -> Start Loop
        - Loop from 2 to n
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
def print_prime_nums(p_num):
    for i in range(2, p_num):
        print(i, end=" ") if is_prime(i) else ...


# Main function having control of the program
def main():
    n = int(input("Enter n: "))
    print("Prime Numbers from 1 to ", n, ":", end=" ")
    print_prime_nums(n)


# Driver's code
if __name__ == "__main__":
    main()
