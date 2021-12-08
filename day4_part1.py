#!/usr/bin/python

import pprint
from collections import Counter

def count_me(inp, score):
  return int(inp)

def scoring(winning_board):
  score = 0
  for row in winning_board:
    for s in row:
      if s != 'x':
        score += int(s)
  return score

def calc_score(bingo_board):
  for board, bingo in bingo_board.items():
    y_count = Counter()
    for xpos, row in enumerate(bingo):
      for ypos, y in enumerate(row):
        if y == 'x': 
          y_count[f'x{xpos}'] += 1
          y_count[f'y{ypos}'] += 1
      returnable = [k for k,v in y_count.items() if v >= 5]
      if returnable: 
        print(y_count)
        return board, bingo
        
def mark_x(number):
  return "x"

def mark_board(number, bingo_board):
  for board, bingo in bingo_board.items():
    for row in bingo:
      for pos, r in enumerate(row):
        if r == number:
          row[pos] = mark_x(r)

def main():

  with open("final_input") as f:
    attempt = f.read()

  numbers_called = []

  bingo_board = {}
  board_counter = 0
  working_board = []
  for a in attempt.split('\n'):
    if ',' in a:
      numbers_called = a.split(',')
    elif a:
      working_board = a.split()
      bingo_board.setdefault(board_counter, []).append(working_board)
    else:
      working_board = []
      board_counter += 1

  for number in numbers_called:
    mark_board(number, bingo_board)
    output = calc_score(bingo_board)
    if output: 
      print(output)
      print(int(number) * scoring(output[1]))
      break
  
  #pprint.pprint(bingo_board)
  #calc_score(bingo_board)

if __name__ == "__main__":
  main()
