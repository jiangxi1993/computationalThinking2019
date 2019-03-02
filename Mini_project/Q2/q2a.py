# q2a.py
# Name:  JIANG XI
# Section: G5

# TODO: fill sv_iterative
# m is a matrix represented by a 2D list of integers. e.g. m = [[3, 0, 2, 18],
#                                                               [-1, 1, 3, 4],
#                                                               [-2, -3, 18, 7]]
# This function returns the Special Value of the matrix passed in.
import copy

def sv_iterative(m):
  x_start=len(m)-1
  y_start=len(m[0])-1
  n=copy.deepcopy(m)
  for j in range(y_start, -1, -1):
    for i in range(x_start, -1, -1):  
      if  i==x_start and j==y_start:
        n[i][j]=m[i][j]
      elif i==x_start and j!=y_start:
        n[i][j]=(n[i][j+1])+(m[i][j])
      elif i!=x_start and j==y_start:
        n[i][j]=(n[i+1][j])+(m[i][j])
      elif i!=x_start and j!=y_start:
        n[i][j]=n[i][j+1]+n[i+1][j]+m[i][j]

  return n[0][0]
  
  
  
  
  
 
