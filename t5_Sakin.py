#####  Store your name, email, student_id and class_number as STRINGS datatype #####
from email import policy


exercise = "Data Structure"
name = "Sakin Khan"
np_email = "S10239867@connect.np.edu.sg"
student_id = "S10239867"
class_number = "TB03"

########################
# Data Structure - LIST
########################

# You are given information of the number of students 
# and school fees of the polytechnics.
# The information is a nested list `polys_info`. 
# The elements in each sub-list contain: 
    ## 1. The institution name
    ## 2. The number of students
    ## 3. Yearly school fee per student

polys_info = [['SP', 4300, 8545], ['NP', 4550, 8650], ['NYP', 4800, 8200], ['RP', 3050, 9050], ['TP', 5200, 8490]]

# 1.
# Write a function `enrollment_summary` with a single parameter `option`. 
# When `1` is supplied to the parameter, `enrollment_summary` will return 
# the total number of students across the polytechnics. 
# When `2` is supplied to the parameter, `enrollment_summary` will return 
# the total school fees revenue collected across the polytechnics. 
# It will return `invalid entry` for any other numbers or strings.


# Creating the function and defining it 
def enrollment_summary(option):
    '''
    Creates dictionary enrollment_summary
    Output a dictionary with kets which are 2 lists named total_students & total_fees
    '''
    # Creates empty lists, total_students & total_fees and store the values in them 
    total_students = []
    total_fees = []

    if option == 1:
        for students in polys_info:
            # Appends index value 1  total_students 
            total_students.append(students[option])
        # Sums up the number of students and returns when option value is 1
        return (f"Total number of Students across the polytechnics: {sum(total_students)}")
    elif option == 2:
        for students in polys_info:
            # Appends index value 2 to total_fees
            total_fees.append(students[option] * students[1])
            # Sums up the total school fees revenue and returns when option value is 2
        return (f"Total school fees revenue collected across the polytechnic: ${sum(total_fees)}")
    else:
        # When option is not 1 or 2, it would return Invalid Entry, to make the user input the correct values of option
         return ("Invalid Entry")

# Creates a variable option and assigns a value of 1 to it
option = 1
# Creates a variable result and assign the value of option and calls the function
result = enrollment_summary(option)
# Prints the varibale, result
print(result)
# Creates a variable option and assigns a value of 2 to it
option = 2
# Creates a variable result and assign the value of option and calls the function
result = enrollment_summary(option)
# Prints the variable, result
print(result)


# 2.`mean`    
# Write a function `mean` with a single parameter `option`. 
# When `1` is supplied to the parameter, `mean` will return the average number of students 
# across the polytechnics
# When `2` is supplied to the parameter, `mean` will return the average school fees revenue
# collected across the polytechnics. 
# Round the return values to 2 decimal places

# Creates a function and defines it 
def mean(option):
    '''
    Creates dictionary mean
    Output a dictionary with kets which are 2 lists named average_students & average_fees 
    '''
    # Creates two empty lists, average_students & average_fees
    average_students = []
    average_fees = []
     
    if option == 1:
        # Appends index value of 1 to average_students 
        for students in polys_info:
            average_students.append(students[option])
        # Returns mean, = sum of total student/ no of polytechnics (len(average_student)) 
        return(f"Average number of students: {sum(average_students)/ len(average_students):.2f}")
    elif option == 2:
        # Appends index value of 2 to average_students 
        for students in polys_info:
            average_fees.append(students[1] * students[2])
        # Returns mean, = sum of average_fees / len(average_fees) 
        return(f"Average school fees revenue: ${sum(average_fees)/ len(average_fees):.2f}")

# Creates a variable option and assigns a value of 1 to it
option = 1
# Creates a variable result and assign the value of option and calls the function
result = mean(option)
# Prints the varibale, result
print(result)
# Creates a variable option and assigns a value of 2 to it
option = 2
# Creates a variable result and assign the value of option and calls the function
result = mean(option)
# Prints the variable, result
print(result)

        
# 3.`median`
# Write a function `median` with a single parameter `option`. 
# When `1` is supplied to the parameter, `median` will return the 
# median number of students of the polytechnics
# When `2` is supplied to the parameter, `median` will return the 
# median yearly school fees of the polytechnics. 

# Creates and define the function 
def median(option):
    '''
    Creates dictionary median
    Output a dictionary with kets which are 2 lists named median_students & median_fees 
    '''
    # Creates to empty lists, median_students and median_fees
    median_students = []
    median_fees = []

    if option == 1:
        for students in polys_info:
            # Appends index value of 1 to median_students
            median_students.append(students[1])
            # finds length of median_students
            n = len(median_students)
            # Sorts the list 
            median_students.sort()
            if n % 2 == 0:
                median1 = median_students[n // 2]
                median2 = median_students[n // 2 - 1]
                median = [(median1 + median2) / 2]
            else:
                median = median_students[n//2]
               # Returns median number of students
        return (f"Median number of students: {median}")

    elif  option == 2:
        for students in polys_info:
            # Appends index value of 2 to median_fees
            median_fees.append(students[2])
            # Finds length of median_fees
            n = len(median_fees)
            # Sorts the list
            median_fees.sort()
        if n % 2 == 0:
            median1 = median_fees[n // 2]
            median2 = median_fees[n // 2 - 1]
            median = [(median1 + median2) / 2]
        else: 
            median = median_fees[n // 2]
            # Returns median yearly school fees
        return (f"Median yearly school fees: ${median} ")

# Creates a variable option and assigns a value of 1 to it
option = 1
# Creates a variable result and assign the value of option and calls the function
result = median(option)
# Prints the varibale, result
print(result)
# Creates a variable option and assigns a value of 2 to it
option = 2
# Creates a variable result and assign the value of option and calls the function
result = median(option)
# Prints the variable, result
print(result)

# Executing the functions will display and return:

    ## print(enrollment_summary(1))
    ## Total number of students across the polytechnics: 21900

    ## print(enrollment_summary(2))
    ## Total school fees revenue collected across the polytechnics: $187211500

    ## print(mean(1))
    ## Average number of students: 4380.0

    ## print(mean(2))
    ## Average school fees revenue: $37442300.0

    ## print(median(1))
    ## Median number of students: 4550

    ## print(median(2))
    ## Median yearly school fees: $8545

# Test 
# def enrollment_summary(option):
#     index = 0 
#     total = 0
#     while index < 5:
#         total += polys_info[index][1]
#         index += 1
#     return total
    
# print(enrollment_summary(1))
