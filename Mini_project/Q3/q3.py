# q3.py
import itertools as iter
# Name: JIANGXI
# Section: G5


# TODO: fill ttsum
# nums is a list of integers (e.g. [3, 0, 1, 0, -1, -2, 0])
# t is the target sum (e.g. 0)
def ttsum(nums, t):
  # your code here
  CombinationList=[]
  CombinationList=find_sumOfTwo(nums, t)+find_sumOfThree(nums, t)
  return CombinationList


def find_sumOfTwo(nums, t):
  result2=[]
  list_of_index=range(len(nums))
  for item in iter.combinations(list_of_index,2):
    #print(item)
    if nums[item[0]]+nums[item[1]]==t:
      result2.append(list((item[0],item[1])))
#  print(result2)
  return result2



def find_sumOfThree(nums, t):
   result3=[]
   list_of_index=range(len(nums))
   for item in iter.combinations(list_of_index,3):
     if nums[item[0]]+nums[item[1]]+nums[item[2]]==t:
       result3.append(list((item[0],item[1],item[2])))
  # print(result3)
   return result3
