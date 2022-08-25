#####  Store your name, email, student_id and class_number as STRINGS #####

ind_assign1 = "challenge 1"
name = "Sakin Khan"
np_email = "S10239867@connect.np.edu.sg"
student_id = "S10239867"
class_number = "TB03"

# Write a function : valid_pin(pin ) with a parameter : pin to test if a string contains a valid pin.  
# A valid pin should contain exactly 8 or 14 characters.   

#The function should return True or False when the "pin" parameter is supplied with the following passwords:

# print(valid_pin("tgif1234"))
# True
# print(valid_pin("01234567890123"))
# True
# print(valid_pin("8afg9abc1"))
# False
# print(valid_pin("9876"))
# False


# Defines and creates a fuction, valid_pin with parameter, pin which returns if the pin is valid or not. 
def valid_pin(pin):
    """
    Function accepts 1 paramter, pin 
    and returns True or False depending on the no of characters == 8 or == 14
    """
    # len(pin) gives you the number of charcters within the parameter, pin
    pin = len(pin)
    # When no. of charcters of pin is 8 or 14, True would be returned 
    if pin == 8 or pin == 14:
        return ("True") 
    # If no of characters is not 8 or 14, False would be returned 
    else: 
        return ("False") 
# Calls the function and prints the value, True or False, for values within the parameter in the function 
print(valid_pin("tgif1234"))
print(valid_pin("01234567890123"))
print(valid_pin("8afg9abc1"))
print(valid_pin("9876"))