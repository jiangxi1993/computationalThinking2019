# q1.py
# Name: JIANG XI
# Section: G5

import random
import math
# TODO: fill r6_loaded()
def r6_loaded():
  # your code here
  # x=random.random() 
  x=random.randint(1, 10)
  #print(x)
  if x<=5:
    return 1
  if x<=6:
    return 2
  if x<=7:
    return 3
  if x<=8:
    return 4
  if x<=9:
    return 5
  else: 
    return 6
  
def r6_loaded_rand():
  # your code here
  x=random.random() 
 # x=random.uniform(0, 10)
  #print(x)
  if x<=0.5:
    return 1
  if x<=0.6:
    return 2
  if x<=0.7:
    return 3
  if x<=0.8:
    return 4
  if x<=0.9:
    return 5
  else: 
    return 6
  
  

