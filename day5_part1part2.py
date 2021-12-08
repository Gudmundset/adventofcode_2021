#!/usr/bin/python

import numpy as np

from pprint import pprint

def part1():
  with open("final_input") as f:
    attempt = f.read()
  inp = attempt.split('\n')

  matrix = np.zeros((1000,1000), int)
  for i in inp:
    x, y = i.split(' -> ')
    x1, y1 = x.split(',')
    x2, y2 = y.split(',')
    if (x1 == x2):
      line = sorted([int(y1),int(y2)])
      print(x1,line)
      x1 = int(x1)
      for ypos in range(line[0], line[1]+1):
        ypos = int(ypos)
        matrix[ypos][x1] += 1
    if (y1 == y2):
      line2 = sorted([int(x1),int(x2)])
      print(y1,line2)
      y1 = int(y1) 
      for xpos in range(line2[0], line2[1]+1):
        xpos = int(xpos)
        matrix[y1][xpos] += 1
  pprint(matrix)
  print(np.count_nonzero(matrix))
  result = np.where(matrix >= 2)
  print(len(result[1]))

def xy_range(start, end):
    (x1, y1), (x2, y2) = start, end
    xsign, ysign = (x2 > x1)*2 - 1, (y2 > y1)*2 - 1
    xrange = range(x1, x2+xsign, xsign) if x1 != x2 else (x1,)*(abs(y2-y1) + 1)
    yrange = range(y1, y2+ysign, ysign) if y1 != y2 else (y1,)*(abs(x2-x1) + 1)
    return zip(xrange, yrange)

def part2():
  with open("final_input") as f:
    attempt = f.read()
  inp = attempt.split('\n')

  matrix = np.zeros((1000,1000), int)
  for i in inp:
    x, y = i.split(' -> ')
    x1, y1 = x.split(',')
    x2, y2 = y.split(',')
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    distance = xy_range((x1, y1), (x2, y2))
    for d in distance:
      matrix[d[0]][d[1]] += 1
      
  pprint(matrix)
  result = np.where(matrix >= 2)
  print(len(result[1]))

if __name__ == "__main__":
  part1()
  part2()
