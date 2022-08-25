#####  Store your name, email, student_id and class_number as STRINGS #####

ind_assign1 = "challenge 2"
name = "Sakin Khan"
np_email = "S10239867@connect.np.edu.sg"
student_id = "S10239867"
class_number = "TB03"

# Write a function : bp(systolic, diastolic) with two parameters : systolic, diastolic to evaluate the blood pressure category.
# When the function is executed, it should return the correct blood pressure category shown in the table above.
# print(bp(110, 75)))
# <Systolic 110> <Diastolic 75> : Normal
# print(bp(124, 77))
# <Systolic 124> <Diastolic 77> : Elevated
# print(bp(134, 80))
# <Systolic 134> <Diastolic 80> : Hypertension Stage 1
# print(bp(150, 100))
# <Systolic 150> <Diastolic 100> : Hypertension Stage 2
# print(bp(181, 100))
# <Systolic 181> <Diastolic 100> : Hypertension Crisis


# Defines and creates a function, bp with parameters systolic and diastolic which returns the blood pressure category
def bp(systolic, diastolic):
    """ 
    Function accepts 2 parameters, systolic & diastolic
    It returns the blood pressure categories depending on the systolic and diastolic number supplied to the parameters
    """
    # Start of infinite loop
    while True:
        # for systolic values lesser than 120 while diastolic values lesser than 80,  <Systolic 110> <Diastolic 75> : Normal would be printed when parameter values 110, 75 are assinged to function
        if systolic < 120 and diastolic < 80:
            return (f"<Systolic {systolic} > <Diastolic {diastolic}> : Normal") 
        # else if systolic values greater than 120 and lesster than 129 while diastolic values is less than 80, <Systolic 124> <Diastolic 77> : Elvated would be printed when parameter values 124, 77 are assinged to function
        elif (systolic >= 120 and systolic <= 129) and diastolic < 80:
            return (f"<Systolic {systolic}> <Diastolic {diastolic}>  : Elevated")
        # else if systolic values greater than 130 and lesster than 139 while diastolic values is greater than 80 or lesser than 89, <Systolic 134> <Diastolic 80> : Hypertension State 1 would be printed when parameter values 134, 80 are assinged to function
        elif (systolic >= 130 and systolic <= 139) and (diastolic >= 80 or diastolic <= 89):
            return (f"<Systolic {systolic}> <Diastolic {diastolic}>  : Hypertension Stage 1")
        # else if systolic values greater than 180 or diastolic values is greater than 120, <Systolic 181> <Diastolic 100> : Hypertension Crisis would be printed when parameter values 181, 100 are assinged to function
        elif systolic > 180 or diastolic > 120: 
            return (f"<Systolic {systolic}> <Diastolic  {diastolic}> : Hypertension Crisis")
         # else if systolic values greater than 140 or diastolic values is greater than or equal to 90, <Systolic 150> <Diastolic 100> : Hypertension Crisis would be printed when parameter values 181, 100 are assinged to function
        elif (systolic >= 140) or (diastolic >= 90): 
            return (f"<Systolic {systolic}> <Diastolic {diastolic}> : Hypertension Stage 2")
    
# Calls the functions and prints it when parameter values are assinged        
print(bp(110, 75))
print(bp(124, 77))
print(bp(134, 80))
print(bp(150, 100))
print(bp(181 , 100))