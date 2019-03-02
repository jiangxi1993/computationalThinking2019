# Name:
# Section:
 
# lab4(a)

# Takes in an integer and returns the sum of all its digits as an integer
# this method does NOT have to handle negative numbers (i.e. i will always be >=0)
# this method must be recursive (i.e. it will call itself)
# Refer to hints in the requirements doc.
def sum_of_digits(n):
  if n == 0: 
    return 0
  return (n % 10 + sum_of_digits(int(n//10))) 

