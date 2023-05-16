def main():
    """
    The function prompts the user to input their first and last name, and then calls another function to
    print their full name.
    """
    f_Name = input("What's first name? ")
    l_Name = input("What's last name? ")
    print_full_name(f_Name, l_Name)


def print_full_name(first, last):
    """
    The function "print_full_name" prints a greeting message with the inputted first and last name,
    followed by a message "You're welcome." in Python.

    :param first: The first name of the person
    :param last: The last name of the person whose full name is being printed
    """
    print("Hello {} {}! You just delved into python.".format(first, last))
    print("You're welcome.")


# `if __name__ == "__main__":` is a conditional statement that checks if the current module is being
# run as the main program. If it is, then it calls the `main()` function, which is the entry point of
# the program. This allows the code to be imported as a module into another program without running
# the main function.
if __name__ == "__main__":
    main()
