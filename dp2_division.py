# This code block is checking if the current script is being run as the main program (as opposed to
# being imported as a module into another program). If it is being run as the main program, it prompts
# the user to input values for variables `a` and `b`, then prints the result of integer division (`a
# / / b`) and regular division (`a / b`).

if __name__ == "__main__":
    a = int(input("What's a? "))
    b = int(input("What's b? "))
    print("a // b =", a // b)
    print("a / b =", a / b)
