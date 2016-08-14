def solve_queens():
  queens = []
  grid_size = 8
  queen = 0
  while queen < grid_size:
    position = 0
    placed = False
    while position < grid_size:
      if len(queens) == 0:
        queens.append([queen, position])
        queen += 1
        placed = True
      if placed == True:
        break
      invalid = False
      for old_queen in queens:
        # Check for conflicts conflict occurs
        if old_queen[1] == position or (abs(old_queen[0] - queen) == abs(old_queen[1] - position)):
          invalid = True
          break
          # If it was not placed and nothing was put in the current column, move back
      if invalid and position == grid_size - 1:
        backtrack = True
        while backtrack:
          queen -= 1
          previous_queen = queens.pop()
          position = previous_queen[1]
          if previous_queen[1] < grid_size - 1:
            placed = False
            backtrack = False

      if invalid == False:
        queens.append([queen, position])
        placed = True
        queen += 1
        position = 0

      else:
        position += 1
        if position >= grid_size:
          queen += 1

  return queens

print(solve_queens())
