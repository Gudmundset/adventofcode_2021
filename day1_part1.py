#!/usr/bin/python
from pprint import pprint

results = []

with open("real_input", 'r') as f:
  attempt = f.readlines()

#print(len(attempt))

for no, a in enumerate(attempt):
  current = int(a.strip('\n'))
  #print(current)
  if no > 0:
    previous = int(attempt[no-1])
    if previous > current:
      results.append(f"{current}: (decreasing)")
      continue
    elif previous < current:
      results.append(f"{current}: (increasing)")
      continue
  results.append(f"{current}: (N/A - no previous measurement)")
pprint(results)
pprint(len([r for r in results if '(increasing' in r]))
