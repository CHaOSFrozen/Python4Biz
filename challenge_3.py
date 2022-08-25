#####  Store your name, email, student_id and class_number as STRINGS #####

ind_assign1 = "challenge 3"
name = "Sakin Khan"
np_email = "S10239867@connect.np.edu.sg"
student_id = "S10239867"
class_number = "TB03"


# Write a function : `employment_salary()` without any parameters.
# The function should return the average monthly salary when executed with:
# print(employment_salary())
# Average monthly salary per employee : $7280.0
# Note: The average monthly salary is computed by summing the monthly salary of each employee before dividing by the number of employees.

employee_info = [['Michael Lee', 8300, 5], ['Ian Wong', 5550, 8], ['Michelle Tan', 7500, 11], ['Adam Koh', 3050, 2], ['Candice Yap', 12000, 12]]

# Creates a function and defines it. It returns when monthly salary when called to action.
def employment_salary():
    """ 
    Function has no given parameter,
    returns the average salary of all employees by accessing the info in given list. 
    """
    # Creates a empty list, average_salary
    average_salary = []
    for es in employee_info:
        # Appends the index value of 1, the monthly salary to average_salary
        average_salary.append(es[1])
    # Creates a variable, average which results in the average monthly salary by adding up all the monthly salary divide by the total number of employee
    average = sum(average_salary)/len(average_salary)
    # Creagtes a variable message which results in the statement "Average monthly salary per employee : $7280.0"
    message = (f"Average monthly salary per employee: ${str(average)}")
    # Returns this message
    return message
# Prints question 1 to differeniate from question 2
print("Question 1: Nested list")
# Creates a variable, result which equates to employment_salary with no parameters assinged to it
result = employment_salary()
# Prints the variable, result, executing the function 
print(result)


# Write a function : `employment_dict()` without any parameters.
# The function will return the average monthly salary when executed with:
# print(employment_dict())
# Average monthly salary per employee : $7280.0
# Note: The average monthly salary is computed by summing the monthly salary of each employee before dividing by the number of employees.


employee_dict = { 
    "Michael Lee" : {"Monthly Salary" : 8300, "Years of Employment" : 5},
    "Ian Wong" : {"Monthly Salary" : 5550, "Years of Employment" : 8},
    "Michelle Tan" : {"Monthly Salary" : 7500, "Years of Employment" : 11},
    "Adam Koh" : {"Monthly Salary" : 3050, "Years of Employment" : 2},
    "Candice Yap" : {"Monthly Salary" : 12000, "Years of Employment" : 12}
    }


def employment_dict():
    """
    Function has no given parameter, 
    returns the average monthly salary of all employees by accessing the nested dict.
    """
    # Creates two variables, total & employeeCount and assigns the value zero
    total = 0
    employeeCount = 0
    for index in employee_dict:
        # creates a new variable, total which gives you increments total, giving you the total monthly salary of all the employees. [KEY] = "Monthly Salary"
        total += (employee_dict[index]["Monthly Salary"]) 
        # creates a new variable, employeeCount which increments employeeCount, rasing the value of each employeecount by 1 until the total number of employees have been acheieved
        employeeCount += 1
    #average monthly salary would be the total salary/ no.of employee
    average = total / employeeCount
    # Creagtes a variable message which results in the statement "Average monthly salary per employee : $7280.0"
    message = (f"Average monthly salary per employee: ${str(average)}")
    # returns message
    return message
# Prints question 2 to differeniate from question 1
print("Question 2: Nested Dictionary")
# Creates a variable, result which equates to employment_salary with no parameters assinged to it
result = employment_dict()
# Prints the variable, result, executing the function 
print(result)