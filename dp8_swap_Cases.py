# string given
# convert the cases of string
# if uppercase, convert to lowercase and vice versa


"""
!START
? ------------ Input ----------------
Muhammad HAMMAD
? ------------ Output ----------------
mUHAMMAD hammad
!END
"""

"""
? -------> Pseudocode
-> Get the string
-> Loop through the string
-> check if the character is lowercase or not
    - if yes, convert to uppercase
    - if no, convert to lowercase
-> return the string
"""


# Main function with all functionality
def main():
    org_str = input("What's string? ")
    swap_str = swap_cases(org_str)
    print("{} -> {}".format(org_str, swap_str))


# Function to swap the case of the string
def swap_cases(string):
    new_str = ""
    for char in string:
        new_str += new_str.join(change_cases(char))
    return new_str


# Function to change the case of the character
def change_cases(char):
    if char.islower():
        return char.upper()
    else:
        return char.lower()


# Driver's code
if __name__ == "__main__":
    main()
