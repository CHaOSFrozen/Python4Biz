#####  Store your name, email, student_id and class_number as STRINGS datatype #####
exercise = "functions and loops"
name = "Sakin Khan"
np_email = "S10239867@connect.np.edu.sg"
student_id = "S10239867"
class_number = "TB03/18"

###################################################################################
# Q1 
# Write a program that allow users to input temperature and convert temperature 
# from Degrees Celsius to Fahrenheit and vice versa. 
# The program should include 2 functions:

    ## cel_to_fahren() 
    # it converts Degrees Celsius to Fahrenheit using celsius * 9/5 + 32

    ## fahren_to_cel()
    #  it converts Fahrenheit to Degrees Celsius using (fahrenheit - 32) * 5/9

# Both functions will round decimals to 2 decimal places.

# When `print(cel_to_fahren())` and `print(fahren_to_cel())` is executed, it should display and return:

    ## Enter temperature in Degrees Celsius: 0.55
    ## Temperature in Fahrenheit: 32.99
      
    ## Enter temperature in Fahrenheit: 10.55
    ## Temperature in Celsius: -11.92

# note that 0.55 and 10.55 are user input

# This defines/creates the fuction without any parameter attached
def cel_to_fahren():  
    # What the function does/ ask the user to input answer in degrees celsius
 celsius = float(input("Enter temperature in Degrees Celsius: "))
 # Converts celsius to fahrenheit
 fahren = celsius * 9/5 + 32
 # Returns the converted value, fahrenheit 
 return fahren
# Calling the function; gives the temperature in fahrenheit 
print(f"Temperature in Fahrenheit: {cel_to_fahren():.2f}")
# Defines/creates the function without any parameter attached
def fahren_to_cell():
    # Ask user to input the temperature in fahrenheit 
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    # Converts Fahrenheit to Celcius 
    celsius = (fahrenheit - 32 ) * 5/9
    # Returns the converted value, celsius 
    return celsius
# Calling the function; gives the temperature in celsius
print(f"Temperature in Celsius:{fahren_to_cell():.2f}")

###################################################################################
# Q2
# Write a function: deposit_calculator(deposit, interest_rate, no_years).
# The function will accumulate the interest earned per year plus the deposit.

# For example, given a $1000 deposit, 10% interest rate and 5 years, 
# the function will calculate the interest earn in 5 years plus the deposit. 
# When `print(deposit_calculator(1000,0.10,5)` is executed, it should return $1610.51

# Tip to calculate interest earn with deposit: 
# Year 1 = $1100 ($1000 * 1.1)
# Year 2 = $1210 ($1100 * 1.1)
# Year 3 = $1331 ($1210 * 1.1) 
# Year 4 = $1464 ($1331 * 1.1)
# Year 5 = $1610.51 ($1464 * 1.1)

# Round off decimals to 2 decimal places.

# BONUS: Can you use f-strings to include a $ symbol with the return value?

# Creating the function deposit calculator 

# Defines the function (Creating it)
def deposit_calculator(deposit,interest_rate,no_years):
    # "I" is a temporary variable used to store the integer value of the parameter in the range of the for loop, which only has scope within its loops
        for i in range(no_years):
            # loops the value, accumalting the interest earned per year plus the  deposit 
            amount = deposit * (interest_rate + 1)
            deposit = amount
        # Returns the amount (updated variable)
        return amount
# Prints and gives the answer rounded of the nearest 2 dps.
print(f"$ {deposit_calculator(1000,0.10,5):.2f}")


    
