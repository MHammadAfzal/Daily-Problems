# Describe the use of lambda
# Short form of a function like arrow function in JS


def main():
    square = lambda x: x * x
    mod = lambda x: x if (x >= 0) else -x
    max = lambda a, b: a if (a > b) else b

    print("The square of  -3: {}".format(square(-3)))
    print("The modulus of -3: {}".format(mod(-3)))
    print("The max  of  3, 5: {}".format(max(3, 5)))


if __name__ == "__main__":
    main()
