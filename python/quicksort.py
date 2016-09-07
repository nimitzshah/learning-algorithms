def quicksort(arr):
  count = len(arr)
  quicksort_call(arr, 0, count -1)
  return arr

def quicksort_call(arr, low, high):
  if(low < high):
    pivot = partition(arr, low, high)
    quicksort_call(arr, low, pivot-1)
    quicksort_call(arr, pivot, high)

def partition(arr, low, high):
  pivot = arr[high]
  j = i = low

  while(j < high):
    if(arr[j] <= pivot):
      arr[j], arr[i] = arr[i], arr[j]
      i += 1
    j += 1

  arr[high], arr[i] = arr[i], arr[high]

  return i

print(quicksort([1,4,4,2,9,6,5,7,8]))
