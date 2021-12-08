#!/usr/bin/python
from collections import Counter

def part1():
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

def part2():
  gamma = ""
  epsilon = ""
  oxygen_generator_rating = ""
  co2_scrubber_rating = ""
  
  with open("final_input") as f:
    attempt = f.read()
  iterable = attempt.split('\n')
  halfway = len(iterable) / 2
  for i in range(len(iterable[0])):
    c = Counter()
    for no, a in enumerate(iterable):
      c[i] += int(a[i])
    most_common = c.most_common()[0][1]
    if most_common >= halfway:
      gamma += "1"
      epsilon += "0"
    else:
      gamma += "0"
      epsilon += "1"
  the_list = iterable
  the_list2 = iterable
  for no, num in enumerate(gamma):
    the_list = [t for t in the_list if t[no] == num]
    if the_list:
      oxygen_generator_rating = the_list[-1]
  for no, num in enumerate(epsilon):
    the_list2 = [t for t in the_list2 if t[no] == num]
    if the_list2:
      co2_scrubber_rating = the_list2[-1]
  oxygen_generator_rating = int(oxygen_generator_rating, 2)
  co2_scrubber_rating = int(co2_scrubber_rating,2)
  print(oxygen_generator_rating * co2_scrubber_rating)

if __name__ == "__main__":
  part1()
  part2()
