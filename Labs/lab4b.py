# Name: 
# Section:
 
# lab4(b) 

# Takes in a base-10 integer and returns the base-2 (binary) equivalent as a string
# this method does NOT have to handle negative numbers (i.e. d will always be >=0)
# this method must NOT use Python's bin() function.
# this method must be recursive (i.e. it calls itself)
# there should not be leading zeros in the string that this method returns.
def to_binary(d):
  if d == 0:
        return ""

  return to_binary(d>>1)+str(d&1)



