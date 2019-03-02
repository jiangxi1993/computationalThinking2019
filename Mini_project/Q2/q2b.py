# q2b.py
# Name: JIANG XI
# Section: G5
import copy
# TODO: fill sv_recursive
# m is a matrix represented by a 2D list of integers. e.g. m = [[3, 0, 2, 18],[-1, 1, 3, 4],[-2, -3, 18, 7]]
# This function returns the Special Value of the matrix passed in.
def sv_recursive(m):
  # your code here
  y = copy.deepcopy(m)
  for i,di in enumerate(m):
    for j, ji in enumerate(di):
      y[i][j] = sv(m,i, j)

  #print(m)
  #print(y)
  return y[0][0]


def sv(d, x, y):
 s = d[x][y]
 b = 0 if x + 1 >= len(d)  else sv(d, x+1, y)
 r = 0 if y + 1 >= len(d[0]) else sv(d, x, y+1)
 return s + b + r
 
