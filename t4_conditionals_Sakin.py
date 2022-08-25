#####  Store your, name, email, student_id and class_number as STRINGS #####
exercise = "conditionals"
name = "Sakin Khan"
np_email = "S10239867@connect.np.edu.sg"
student_id = "S10239867"
class_number = "TB03"

# Part 1
####################################################################################
# Write a function: income_rebate() to prompt a user to declare his/her monthly income 
# and determine the amount of GST rebate the user should receive.
# It will return the amount of GST rebate based on the following evaluation:

# Monthly Income $ 	                GST rebate $
#------------------                 ------------- 
# 0 to less than 2000 	                1000
# 2000 to less than 5000 	            500
# 5000 to less than 10,000 	            250
# equal or greater than 10,000 	     not eligible

#  Executing `print(income_rebate())` will display and return:

    # Declare your monthly income : 500
    # Your GST rebate is : $1000

    # Declare your monthly income : 4000
    # Your GST rebate is : $500
    
    # Declare your monthly income : 7000
    # Your GST rebate is : $250
    
    # Declare your monthly income : 10000
    # You are not eligible for GST rebate
# This creates the function income_rebate
def income_rebate():
    """The code below is utilziing the if, elif functions"""
    # Asks user for their monthly income (Input)
    user_input = int(input("Declare your monthly income: "))
    # For user_input less than 2000, the rebate returned would be 10000
    if user_input < 2000:
        return("Your GST rebate is $1000")
    # IF user_input is less than 5000, the rebate returned would be 500
    elif user_input < 5000: 
        return("Your GST rebate is $500")
    # If user_input is less than 10k, the rebate returned would be 250
    elif user_input < 10000:
        return("Your GST rebate is $250")
    # If user_input is equal to 10k, the user would not be elgible for GST rebate
    else: 
        return("Your are not eligible for GST rebate")
# Prints Question 1 to differentiate the answer from question 2
print("Question 1")
# Prints value of the Income_rebate
print(income_rebate())

# Part 2
####################################################################################
# try except else

# Enhance income_rebate() with `try`, `except` and `else` to make it less 
# susceptible to crash. 
# 
# Name the enhanced function as income_rebate_enhanced().

# The enhancement should prevent `ValueError` from crashing the program.

# Tip: Design the function with while loop in mind. The functions will 
# keep looping until user input enters a number data type.

# Executing `print(income_rebate_enhanced())` should display and return the folllowing
# until the user enters a number data type:

    # Declare your monthly income: ten thousand
    # Invalid input

    # Declare your monthly income: one thousand
    # Invalid input

    # Declare your monthly income: 10
    # Your GST rebate is : $1000

# Creates a function
def enhanced_income_rebate():
    # Start of infinite loop
    while True :
         # Start of expection handling
        try: 
            user_input = int(input("Declare your monthly income: "))
        # Handling of exception
        except ValueError:
            # Prints out error message
            print("Your input is invalid, please try again")
        # When expection does not occur 
        else: 
            if user_input < 2000:
                return("Your GST rebate is $1000")
            # IF user_input is less than 5000, the rebate returned would be 500
            elif user_input < 5000: 
                return("Your GST rebate is $500")
             # If user_input is less than 10k, the rebate returned would be 250
            elif user_input < 10000:
                return("Your GST rebate is $250")
            # If user_input is equal to or greater to 10k (None of the above), the user would not be elgible for GST rebate
            else: 
                return("Your are not eligible for GST rebate")
# Prints ( Question 2 to differiate the answers )
print("Question 2")
# Prints enhanced_income_rebate
print(enhanced_income_rebate())
        