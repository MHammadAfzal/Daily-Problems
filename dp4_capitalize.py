def main():
    """
    This function prompts the user for a name, capitalizes it, and then prints the capitalized name.
    """
    str = input("What's name? ")
    cap_str = capitalize(str)
    print(cap_str)


def capitalize(str):
    """
    The function capitalizes the first letter of each word in a given string.

    :param str: a string that contains one or more words separated by spaces
    :return: The function `capitalize` returns a string where the first letter of each word in the input
    string `str` is capitalized.
    """

    # This line of code is capitalizing the first letter of each word in the input string `str`.
    str = " ".join([name.capitalize() for name in str.split(" ")])
    return str


# `if __name__ == "__main__":` is a conditional statement that checks if the current script is being
# run as the main program. If it is, then the `main()` function is called, which is the entry point of
# the program. This allows the script to be imported as a module into another program without running
# the main function.
if __name__ == "__main__":
    main()
