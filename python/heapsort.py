def heapsort(numbers):
  count = len(numbers)
  heapify(numbers, count)

  end = count - 1
  while(end > 0):
    numbers[end], numbers[0] = numbers[0], numbers[end]
    end -= 1
    sift_down(numbers, 0, end)

  return numbers

def heapify(numbers, count):
  start = (count - 1)//2 # starting parent is here.
  while(start >= 0 ):
    sift_down(numbers, start, count-1)
    start -= 1

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


numbers = [3,2,1,5,4,0,9,6,7,8,8,12,3,4,1,2,5,6,3,1,-3,-5,-6]

print(heapsort(numbers))
