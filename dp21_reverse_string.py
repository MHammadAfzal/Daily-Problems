# Get a string from user
# Reverse the string
# Print the reversed string


"""
!START
? ---------- Input -------------
Input : CS quiz practice code
Input : my name is Hammad
? ---------- Output -------------
Output : code practice quiz CS
Output : Hammad is name my
!END
"""

"""
? -------------> Pseudocode
=> Get a string from user namely str
=> Call the function to reverse the string
    -> 
=> print the resultant string
"""


def reverse_str(string):
    string = string.split()
    res = (string.pop() for i in range(len(string)))
    return " ".join(res)


def main():
    user_str = input("What's the string? ")
    user_str = reverse_str(user_str)
    print("-----> Reversed String: {}".format(user_str))


if __name__ == "__main__":
    main()
