#!/usr/bin/python
from pprint import pprint

results = []

with open("real_input", 'r') as f:
  attempt = f.readlines()

#print(len(attempt))

for no, a in enumerate(attempt):
  current = int(a.strip('\n'))
  try:
    currentsum = int(attempt[no]) + int(attempt[no+1]) + int(attempt[no+2])
  except:
    break #exit loop, reached end of sliding window
  if no > 0:
    previous = int(results[no-1].split(':')[0])
    if previous > currentsum:
      results.append(f"{currentsum}: (decreased)")
      continue
    elif previous < currentsum:
      results.append(f"{currentsum}: (increased)")
      continue
    elif previous == currentsum:
      results.append(f"{currentsum}: (no change)")
  else:
    results.append(f"{currentsum}: (N/A - no previous measurement)")

pprint(results)
pprint(len([r for r in results if 'increased' in r]))
