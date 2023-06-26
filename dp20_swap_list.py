# Create an list(array) from user
# identify first and last element of list(array)
# swap first and last element of array
# print the result


"""
!START
? ---------- Input -------------
Input : [12, 35, 9, 56, 24]
Input : [1, 2, 3]
? ---------- Output -------------
Output : [24, 35, 9, 56, 12]
Output : [3, 2, 1]
!END
"""

"""
? -------------> Pseudocode
=> Create an list(array) from user
=> Call function to swap first and last element of array
    -> Identify First Element of list
    -> Identify Second Element of list
    -> Declare some temp variable and swap the elements
    -> Return the swapped array
=> Print the swapped elements in a new line.
"""


def swap_fl(swap_ls):
    temp = swap_ls[0]
    swap_ls[0] = swap_ls[len(swap_ls) - 1]
    swap_ls[len(swap_ls) - 1] = temp


def swap_fl2(swap_ls):
    start, *middle, end = swap_ls
    return [end, *middle, start]


def main():
    ls = [12, 35, 9, 56, 24]
    print("Original List: {}".format(ls))
    swap_fl(ls)
    print("Swapped list is: {}".format(ls))


if __name__ == "__main__":
    main()
