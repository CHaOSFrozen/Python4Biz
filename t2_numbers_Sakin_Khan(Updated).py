#####  Store your, name, email, student_id and class_number as STRINGS #####
exercise = "numbers"
name = "Sakin Khan"
np_email = "S10239867@connect.np.edu.sg"
student_id = "S10239867"
class_number = "TB03"

##################################################################################
# Write a program to ask user to input two numbers separately.                              
# The program will check if the difference between the 2 numbers is an integer. 
##################################################################################

# The program should display the following when executed:

    ## First execution ##
    # Enter first number : 1.5
    # Enter second number : 0.5
    # 1.5 - 0.5 = 1.0
    # Is the difference between 1.5 and 0.5 an integer? True

    ## Second execution ##
    # Enter first number : 2.5
    # Enter second number : 1.3
    # 2.5 - 1.3 = 1.2
    # Is the difference between 2.5 and 1.3 an integer? False

# Assign `num1` for first number, `num2` for second number 
# Assign `diff` as the difference between `num1` and `num2`  


##################################################################################
# Write a program to ask user to input two numbers separately. 
# The program will use the first number as a base number and second number as an exponent.
# The output should return the value when base number is raised to the exponent. 
##################################################################################

# The program should display the following messages :

    # Enter a base number: 2
    # Enter an exponent: 3
    # 2 to the power of 3 is 8

# Assign `num3` for base number and `num4` for exponent.
# Assign 'raise_power` to store the results of the exponent operation.


# Asking the input of variables num1 and num2
num1 = (float(input("Enter first number: ")))
num2 = (float(input("Enter second number: ")))
# Calculated the difference between num1 and num2 and assigning it to a new value
diff = num1 - num2
# Printing the difference as asked in Line 18)
print(f" {num1} - {num2} = {diff}")
# Checking if diff is an integer or a float
print(f"Is the difference between {num1} and {num2} an integer? {diff.is_integer()}")

# Asking the inputs of new values of varibales num1 and num2
num1 = (float(input("Enter first number: ")))
num2 = (float(input("Enter second number: ")))
# Calculating the differenc between each a variable
diff = num1 - num2
# Printing the difference as tasked on line 24
print(f"{num1} - {num2} = {diff}")
# Checking if its a float or a integer
print(f"Is the differnece between {num1} and {num2} an integer? {diff.is_integer()}")

# Asking user to input values for vairables num3 and num4
num3 = (int(input("Enter a base number: ")))
num4 = (int(input("Enter a exponent: ")))
# Calculating the exponent by raising the power
raise_power = num3 ** num4
# Using F strings and print fuction as tasked in line 41
print(f" {num3} to the power of {num4} is {raise_power}")