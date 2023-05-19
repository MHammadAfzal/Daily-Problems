# collection of countries stamps
# to find -> distinct country stamps in her collection
# pick the stamps of her collection one by one
# store it in your collection
# N country stamps

"""
!START
?---------------  Input -----------------
* use Sets for this purpose
n = ["Pak", "Ban", "UK", "Pak", "UK", "USA"]
?---------------  Output -----------------
n = ["Pak", "Ban", "UK", "USA"]
!END
"""

"""
? -----> Psuedocode 
-> get input of how many country stamps are there
-> Enter the names of the countries
-> Add these names in the set
-> The set will automatically eliminate the duplicate names
-> print the names of countries in the set which should be distinct
"""


# main function with all functionality
def main():
    country_set = get_input()
    print_names(country_set)


# Function to get input
def get_input():
    # create an empty set
    return_set = set()
    for _ in range(int(input("How many countries to add? "))):
        # add the countries in the set
        return_set.add(input("Enter the name of the country: "))
    return return_set


# Function to print the names
def print_names(names):
    print("----- {} Distinct Countries ------".format(len(names)))
    for name in names:
        print(name)


# Driver Code
if __name__ == "__main__":
    main()
