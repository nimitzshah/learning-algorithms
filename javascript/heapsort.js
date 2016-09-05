function heapsort (numbers) {
  // First we heapify the numbers
  const size = numbers.length
  heapify(numbers, size)
  var end = size - 1

  while(end > 0){
    let tmp = numbers[0]
    numbers[0] = numbers[end]
    numbers[end] = tmp
    end -= 1
    siftDown(numbers, 0, end)
  }
  return numbers
}

function heapify (numbers, size) {
  start = Math.floor((size -1) /2)
  while(start>= 0){
    siftDown(numbers, start, size -1)
    start -= 1
  }
}

function siftDown(numbers, start, end) {
  var root = start
  var swap = root
  var leftChild = (root * 2) + 1
  while(leftChild <= end){
    if(numbers[swap] < numbers[leftChild]){
      swap = leftChild
    }

    if(leftChild + 1 <= end && numbers[swap] < numbers[leftChild + 1]){
      swap = leftChild + 1
    }

    if(swap === root) {
      return
    } else {
      let tmp = numbers[root]
      numbers[root] = numbers[swap]
      numbers[swap] = tmp
      root = swap
      leftChild = (root * 2) + 1
      console.log(numbers)
    }
  }
}


console.log(heapsort([1,4,2,3,7,6,9,9,8,0]))
