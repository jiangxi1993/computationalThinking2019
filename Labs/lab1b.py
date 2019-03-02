# Name: XI.JIANG.2017
# Section: G5

# lab1b

# fill up the weight_category method to return either "underweight", "overweight" or "normal" 
# depending on the height (in cm) and weight (in kg)
def weight_category(weight, height):
  BMI=weight/((height/100)**2)
 
  if BMI<18.5:
    return "underweight"
  elif BMI>25:
    return "overweight"

  return "normal"
