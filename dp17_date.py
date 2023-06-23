# Print current date
# Print current time


"""
!START
? ---------- Input -------------
-
? ---------- Output -------------
Current date and time : 2023-06-23 14:34:14
!END
"""

"""
? -------------> Pseudocode
=> Import the datetime library
=> Get current time and date from datetime library in some variable
=> Modify the variable in the required format
=> Print the date and time
"""

import datetime


def main():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time: {}".format(now))


if __name__ == "__main__":
    main()
