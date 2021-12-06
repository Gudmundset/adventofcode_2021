#!/usr/bin/python

from collections import Counter

def main():
  gamma = ""
  epsilon = ""
  
  with open("final_input") as f:
    attempt = f.read()
  iterable = attempt.split('\n')
  halfway = len(iterable) / 2
  for i in range(len(iterable[0])):
    c = Counter()
    for no, a in enumerate(iterable):
      c[i] += int(a[i])
    answer = c.most_common()[0][1]
    if answer >= halfway:
      gamma += "1"
      epsilon += "0"
    else:
      gamma += "0"
      epsilon += "1"
  print(int(gamma, 2) * int(epsilon, 2))

  #answer int(target, 2)

if __name__ == "__main__":
  main()
