# Name: <replace with your name>
# Section: <replace with your section>

# lab2b

# INSTRUCTIONS: 
# Refer to the code in lab2b_main.py - perform_once will be called one time before 
# exist is called many times. You may modify perform_once if desired, or keep it as it is.
def perform_once(employee_with_birthyear_list):
  # Write any code here if desired. Any code you do here will replace the original employee_list
  employee_birthyear_dict={}

  for n in range(len(employee_with_birthyear_list)):

    year=employee_with_birthyear_list[n][1]
    id =employee_with_birthyear_list[n][0]

    if employee_birthyear_dict.get(year)==None:
      employee_birthyear_dict[year]=[]

    employee_birthyear_dict[year]+=[id]
   

       
  return employee_birthyear_dict

  
# INSTRUCTIONS: 
# Write a function called get_IDs_with_birthyear that takes in a year (as an integer) and an array (employee_with_birthyear_list)
# It then returns an array of employee IDs (integers) that have matching birthyears.
# If there is no match, this function returns an empty array (i.e. []).
def get_IDs_with_birthyear(year, employee_birthyear_dict):
  return employee_birthyear_dict.get(year,[])
  
  