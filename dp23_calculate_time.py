# Calculate time of a process


"""
!START
? ---------- Input -------------
Input : 0s 
? ---------- Output -------------
Output : some time
!END
"""

"""
? ------------> Pseudocode
=> import time library
=> calculate start time
=> Run the process you wanna run
=> calculate end time
=> subtract start time from end time
=> convert to string and return it as output
"""


import time

for i in range(123):
    print(i)

print(time.time())


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
    start_time = time.time()
    main()
    print("--------------------------")
    time.sleep(2)
    end_time = time.time()
    total_time = str(end_time - start_time)
    print("Total Time: {}s".format(total_time))
