def heapify(numbers):
  count = len(numbers)
  start = (count - 1)//2 # starting parent is here.
  while(start >= 0 ):
    sift_down(numbers, start, count-1)
    start -= 1

  return numbers

def sift_down(numbers, start, end):
  root = start
  left_child = (2 * root) + 1
  while(left_child <= end):
    child = left_child
    swap = root

    if(numbers[child] > numbers[swap]):
      swap = child

    if(child + 1 <= end and numbers[child+1] > numbers[swap]):
      swap = child + 1

    if(swap == root):
      return

    else:
      swapped_number = numbers[swap]
      numbers[swap] = numbers[root]
      numbers[root] = swapped_number
      root = swap
      left_child = (2 * root) + 1
