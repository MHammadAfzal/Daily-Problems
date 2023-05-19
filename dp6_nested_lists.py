# names, grades -> students (N students)
# store these names, grades in nested lists
# print name of students having second-lowest grade
# if 2 students have second-lowest grades order their names alphabetically

"""
!START
?---------------  Input -----------------
* nested list
records = [["Hammad", 40], ["Ali", 40], ["Hassan", 50], ["Ahsan", 60], ["Ahmad", 30]]
? --------------- Output ----------------
Ali
Hammad
!END
"""

"""
? -----> Psuedocode 
-> Create a nested list of records
-> Input how many records the user want to enter
-> Loop through the records

-> Start loop 
-> take inputs user has requested
-> Ask the user for the input of records from user
    - First Ask Name
    - Secondly Ask Grade
-> Store the inputs in records nested list by using append method
    - append by making a nested list like [name, grade]
-> End loop

-> Start loop
-> Check 2nd lowest grade students
-> Identify the students having 2nd lowest grades
-> End loop
-> Print the name of the students having second-lowest grade

"""


# main function with all functionality
def main():
    # get records of n students
    records = get_records()
    # find the second lowest grade among students
    second_lowest_grade = get_second_lowest_grade(records)
    # find the names of student having second lowest grades
    second_lowest_grade_names = get_names(second_lowest_grade, records)
    # print the name of the students having second-lowest grade
    print_names(second_lowest_grade_names)


# Function to get the records of n students
def get_records():
    records = []
    for _ in range(int(input("Enter the number of records: "))):
        records.append(get_inputs())
    return records


# Function to get the inputs of n students
def get_inputs():
    name = input("What's name? ")
    grade = float(input("What's grade? "))
    return [name, grade]


# Function to find the second lowest grade among students
def get_second_lowest_grade(rec):
    return sorted(list(set(x[1] for x in rec)))[1]


# Function to find the names of student having second lowest grades
def get_names(req_grade, records):
    return_list = []
    for name, grade in records:
        return_list.append(name) if grade == req_grade else ...
    return return_list


# Function to print the name of the students having second-lowest grade
def print_names(names):
    print("------- Students with Second Lowest Grades -------")
    for name in sorted(names):
        print(name)


if __name__ == "__main__":
    main()
