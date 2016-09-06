import heap

def heap_extract_max(numbers):
  if(len(numbers) < 1):
    return "Heap underflow"
  maximum = numbers[0]
  count = len(numbers)
  max_number = numbers.pop(0)
  heap.heapify(numbers)
  return max_number

numbers = [1,3,2,6,7,4,3,2]

heap.heapify(numbers)
heap_extract_max(numbers)
print(numbers)
