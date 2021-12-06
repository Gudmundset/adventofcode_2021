#!/usr/bin/python

import operator

def translate_input(command):
  direction, amount = command.split(' ')
  return direction, int(amount)

def main():
  
  z_pos = 0
  y_pos = 0
  command_map = {"forward": operator.add,
                 "down": operator.add,
                 "up": operator.sub,
  }
  with open("final_input") as f:
    attempt = f.read()
  for a in attempt.split('\n'):
    command, value = translate_input(a)
    op = command_map[command]
    if command == 'forward':
      z_pos = op(z_pos, value)
    else:
      y_pos = op(y_pos, value)
  
  print(z_pos * y_pos)

if __name__ == "__main__":
  main()
