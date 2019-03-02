# Name: XI.JIANG.2017
# Section: G5

# lab1a

# fill up the admit method to return either True or False depending on the sex and age
def admit(sex,age):
  if sex == "F" and age>=18:
    return True
  elif sex == "M" and age>=23:
    return True

  return False
