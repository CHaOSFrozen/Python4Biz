#####  Store your name, email, student_id and class_number as STRINGS #####

ind_assign1 = "challenge 4"
name = "Sakin Khan"
np_email = "S10239867@connect.np.edu.sg"
student_id = "S10239867"
class_number = "TB03"


# A fitness wearable device tracks the distance its users walk or run daily. To motivate the users to meet and exceed the target distance, it rewards users with fitness points on a leadership board for the users who meet and exceed the target distance in a week.

# The fitness point is calculated with a minimum distance of 32 km per week, and the points for each km in excess of the minimum distance is show as follow:

# Distance            Fitness Point
# 0 to 32 km          Zero
# 33 to 40 km         325 points per km
# 41 to 48 km         550 points per km
# Greater than 48 km  600 points per km
# The points are calculated progressively. As an example, if a user reached total distance of 45km in a week, the points is computed as follows:
# 32*0 + 8*325 + 5*550 = 5350

 # Write a function : fitness_app(distance) with a parameter : distance. The function should return the calculated fitness points when the distance (in km) is supplied to the parameter.
def fitness_app(distance):
    """
    Function accepts distance, sorts it according to the distance value 
    and returns the total points depending on the distance value.
    """
    # Start of infinite loop 
    while True:
        # When distanc is equal or greater than 0 and lesser or equal to 32, it would return 0 points, 32 * 0.
        if distance >= 0 and distance <= 32:
            points = distance*0
            return points
        # When distance is equal to 33 or lesser or equal to 40, it would return the accumulated points which include 0 points from before. It would also minus the value of the previous highest distance, which would then be times by the number of points, 325
        elif distance >= 33 and distance <= 40:
            points = 32*0 + (distance- 32)*325 
            return points 
        # When distance is equal to 41 or lesser or equal to 48, it would return the accumulated points which include 0 points and the points from distance 32 - 40 from before. It would also minus the value of the previous highest distance, which would then be times by the number of points, 550 
        elif distance >= 41 and distance <= 48:
            points = 32*0 + 8*325 + (distance - 40)*550
            return points 
        # When distance is not equal to any of the requirements above, greater than 4, it would return the accumulated points which include all the points from before. It would also minus the value of the previous highest distance, which would then be times by the number of points, 600
        else: 
            points = 32*0 + 8*325 + 8*550 + (distance - 48)*600
            return points
# Excuates and prints the function with the different parameter values
print(fitness_app(15))
print(fitness_app(37))
print(fitness_app(45))
print(fitness_app(50))
