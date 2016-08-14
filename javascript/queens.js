checkQueens = function(olderQueen, queen, position){
  return Math.abs(olderQueen[0] - queen) == Math.abs(olderQueen[1] - position) || olderQueen[1] == position ? false : true
}

solveQueens = function(gridSize){
  const queens = []
  let queen = 0
  let position = 0
  // Iterate through the queens on each row
  while(queens.length < gridSize){
    position = 0
    let placed = false
    // Iterate through the positions of each queen
    while(!placed){
      let valid = true
      let queenPosition = 0
      let backtrack = true

      if(queens.length == 0){
        queens.push([queen, position])
        queen += 1
      }

      while(valid && queenPosition < queens.length) {
        olderQueen = queens[queenPosition]
        if(!checkQueens(olderQueen, queen, position)) {
          valid = false
        }
        queenPosition += 1
      }

      if(!valid && position >= gridSize -1){
        while(backtrack){
          queen -= 1
          let former_queen = queens.pop()
          position = former_queen[1]
          if(position < gridSize - 1){
            backtrack = false
          }
        }
      }

      if(valid){
        queens.push([queen, position])
        queen += 1
        position = 0
        placed = true
      }else{
        position += 1
        if(position >= gridSize){
          queen += 1
        }
      }
    }
  }
  return queens
}



console.log(solveQueens(8))
