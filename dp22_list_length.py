# Create a list/array
# Find length of list/array
# Print the length of list/array


"""
!START
? ---------- Input -------------
Input : my_list = [1,2,"hammad",4.5, 5]
Input : my_list = [1,2,'Hammad',3.67890, 'Ali', 4.000, 67]
? ---------- Output -------------
Output : length: 5
Output : length: 7
!END
"""

"""
? -------------> Pseudocode
=> Create a list
=> Call the function to find length of a list
    -> Create a variable named counter
    -> Loop through all elements
        - increment counter on each iteration
    -> return counter
=> print out the length of list
"""


def find_len(ls):
    counter = 0
    for i in ls:
        counter += 1
    return counter


def get_lists():
    return ([1, 2, "hammad", 4.5, 5], [1, 2, "Hammad", 3.67890, "Ali", 4.000, 67])


def print_len(len_ls1, len_ls2, head):
    print("--------- Using {} Function -----------".format(head))
    print("The length of list 1: {}".format(len_ls1 if head == "Own" else len(len_ls1)))
    print("The length of list 1: {}".format(len_ls2 if head == "Own" else len(len_ls2)))


def main():
    my_list1, my_list2 = get_lists()
    len_list1, len_list2 = (find_len(my_list1), find_len(my_list2))
    print_len(my_list1, my_list2, "Defined")
    print_len(len_list1, len_list2, "Own")


if __name__ == "__main__":
    main()
