#####  Store your name, email, student_id and class_number as STRINGS datatype #####
exercise = "strings"
name = "sakin khan"
np_email = "s10239867@connect.np.edu.sg"
student_id = "s10239867"
class_number = "18"

######################################################
# Write a program to allow a user to enter some text #
######################################################

# Given the user input text, the program is designed to:
    # 1. Convert any lower case letters to upper case letters
    # 2. Replace any letters A,E,I,O,U with 1,2,3,4,5 respectively.

# When your program file is run, it will display messages like this:

    # Enter a country in lowercase: singapore
    # Converting to upper case letter...SINGAPORE
    # Hit any key to continue...
    # Converting any A,E,I,O,U in your entry to 1,2,3,4,5...S3NG1P4R2

# Note that `singapore` is the user input text.

# Assign a variable `country` to store the user input and continue to use the same variable 
# variable name throughout.


# User input for country
country = input("Enter a country in lowercase: ")
# Print country name 
print("Covering to upper case letter...",country.upper())
# Input Hit any key to continue
input("Hit any key to continue...")
country_new = country.upper()
converted_1 = country_new.replace("A","1")
converted_2 = converted_1.replace("E", "2")
converted_3 = converted_2.replace("I", "3")
converted_4 = converted_3.replace("O","4")
converted_5 = converted_4.replace("U", "5")
# Converts any A,E,I,O,U in my entry to 1,2,3,4,5
print("Converting any A,E,I,O,U in your entry to 1,2,3,4,5...", converted_5)


