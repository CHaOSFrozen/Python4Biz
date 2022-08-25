#####  Store your name, email, student_id and class_number as STRINGS datatype #####
exercise = "individual assignment 2"
name = "Sakin Khan"
np_email = "S10239867@connect.np.edu.sg"
student_id = "S10239867"
class_number = "WB03"

# The following modules are imported to kickstart your assignment:
from pathlib import Path
import re, csv

### Tips for the assignment ###

# 1. Set file paths to pfb_ind_assign2 folder for reading and writing files.
# 2. Create search pattern for rental, address, flat type and date
# 3. Iterate over tenancy documents 
     # For each file open as read mode:
          ## 3.1 search and return rental, address flat type and dates
          ## 3.2 clean up the extracted data 
          ## 3.3 for each matched item, append to tenancy.csv

# Set file paths to pfp_ind_assign2 folder for reading and writing files 
file_path = Path.cwd()/"pfb_ind_assign2"
# check if file_path exists(), returns True or False.
print(file_path.exists())

file_path_tenancycsv = Path.cwd()/"pfb_ind_assign2"/"tenancy.csv" 
# check if file_path exists(), returns True or False.
print(file_path.exists())

# opens files with .open() to return a file object by providing mode and encoding to the parameter, to be able to writer and decode/encode using UTF-8
with file_path_tenancycsv.open(mode="w", encoding = "UTF-8", newline="") as file:
     # Create a writer object and named it as'writer' variable. (instantiate a writer object)
     writer = csv.writer(file)
     # `.writerow()` to write headers that is a list with 5 elements, Create a writer object: 'writer' with `csv.writer()`.
     writer.writerow(["ADDRESS", "FLAT TYPE", "START DATE","END DATE", "RENTAL"])
     file.close()

# allows the search of a certain type of file, "*.txt" through iteration in the folder. (5 Tenancy_Agreement Files) 
for file in file_path.glob("*.txt"):
     # Creates an empty lists and assigns the values that will be appended onto this list later on.
     empty_list = []
     # open file with .open() to return a file object by providing mode and encoding to the parameter, to be able to read and append and decode/encode using UTF-8
     with file.open(mode = "r", encoding = "UTF-8", newline = "") as file:
          # Create a reader object and named it as a "reader" variable (instantiate a read object)
          reader = file.read()
          # Finds the address, flat, start date, end date and rental using search pattern. The "r" before the pattern treats the code as a raw string

          # Find the address by using the search function and supplying a pattern to it. 
          address = (re.search(pattern =r"Block [0-9]+ Unit [0-9]+-[0-9]+ [A-z].+", string = reader)).group()
          # Appends the results of the search to the empyty list 
          empty_list.append(address)

          # Finds the flat type using the search pattern and iterates over the specified iterable and appends its elements to the end of the current list.
          flat_type = re.findall(pattern="[0-9] ROOM FLAT", string = reader)
          empty_list.extend(flat_type)

          date = re.findall(pattern=r"[0-9]+-[0-9]+-[0-9]+", string = reader)
          # Appends incrementation of first value and second value respectively
          first_date = date[0]
          second_date = date[1]
           # Appends the results of the search to the empyty list
          empty_list.append(first_date)
          empty_list.append(second_date)

          # Finds the rental amount using the search pattern and iterates over the specified iterable and appends its elements to the end of the current list.
          rental = re.findall(pattern=r"SGD[0-9]+", string = reader)
          empty_list.extend(rental)
     # open file with .open() to return a file object by providing mode and encoding to the parameter, to be able to append and decode/encode using UTF-8
     with file_path_tenancycsv.open(mode="a", encoding="UTF-8", newline="") as file:
               # Create a writer object: 'writer' with `csv.writer()`.
               writer = csv.writer(file)
               writer.writerow(empty_list)


# Creates a function and defines it 
def mean(option):
    '''
    Creates dictionary mean
    Output a dictionary with kets which are 2 lists named average_students & average_fees 
    '''
    polys_info = "1"
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