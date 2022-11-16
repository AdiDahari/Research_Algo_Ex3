# Research_Algo_Ex1

### Q1 - Email Validator - q1.py
  This question is about email validation
  
  This quetsion solution has 2 parts: 
  
      1. Handling file reading and extracting email-like patterned strings.
      2. Checking email addresses validity by matching each of them to a regular expression.
  
  The final output is a printing of 2 lists: Valid Emails and Invalid Emails.
  
  Provided here you'll find a test file called 'emails.txt'
  which contains a list of valid and invalid emails within sentances and standalone.
  
### Q2 - Last Call - q2.py
  This question is about a decoration of Cached results of functions
    
  The function last_call recieves a function call and checks whether an identical call has been made.
  
  if so - it returns the cached result of the last call with the same set of parameters.
  
  if not - it stores the function's result by its parameters and returns the result.
  
### Q3 - List - q3.py
  
  This question is about creating a class that inherit from built-in type 'list'
  it expands lists functionality by allowing a multi-layered call within a square brackets pair ([]), both for getting items and for setting them.
  
  For example:
  
      lst = [[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 0]]]
      Lst = List([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 0]]])
  
      lst[0][0][0] = 1
      Lst[0, 0, 0] = 1
  
  for any single-layered call it functions the same as list.
  
  
### Q4 - Coding Game solution
  This question is a implementation of a challenge of codingame.com
  
  The challenge: There is no Spoon - Episode 1

  The Solution:
  
    import sys
    import math

    # Don't let the machines win. You are humanity's last hope...

    width = int(input())  # the number of cells on the X axis
    height = int(input())  # the number of cells on the Y axis
    lines = []
    for i in range(height):
        line = input()  # width characters, each either 0 or .
        lines.append(list(line))



    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    for i in range(height):
        for j in range(width):
            if lines[i][j] != '.':
                x1 = x2 = y1 = y2 = -1

                for x in range(j + 1, width):
                    if lines[i][x] == '0':
                        x1 = x
                        y1 = i
                        break
                for y in range(i + 1, height):
                    if lines[y][j] == '0':
                        x2 = j
                        y2 = y
                        break

                print(f'{j} {i} {x1} {y1} {x2} {y2}')

    # Three coordinates: a node, its right neighbor, its bottom neighbor
    print("0 0 1 0 0 1")

        
   Link: https://www.codingame.com/training/medium/there-is-no-spoon-episode-1/solution?id=27238794
   
   Screenshot: 
    ![codingame com - There is no Spoon - Episode 1](https://user-images.githubusercontent.com/71274563/202210275-5a8bb5a6-f135-4142-8256-a27f5414e600.png)

