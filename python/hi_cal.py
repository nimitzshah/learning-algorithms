def hi_cal(list_of_tuples):
  list_of_tuples.sort(key=lambda tup: tup[0])

  merged_tuples = []

  while(len(list_of_tuples) > 0):
    meeting = list_of_tuples.pop(0)

    if(len(merged_tuples) == 0):
      merged_tuples.append(meeting)
    else:
      start = meeting[0]
      end = meeting[1]
      if start == merged_tuples[-1][0]:
        popped = merged_tuples.pop(-1)
        print(meeting, popped)
        if end > popped[1]:
          merged_tuples.append((start, end))
        else:
          merged_tuples.append((start, popped[1]))
      elif start <= merged_tuples[-1][1]:
        popped = merged_tuples.pop(-1)
        print(" start less than or equal to thangs",meeting, popped)
        if end > popped[1]:
          merged_tuples.append((popped[0], end))
        else:
          merged_tuples.append((popped[0], popped[1]))
      else:
        merged_tuples.append(meeting)

  return merged_tuples

list_of_tuples = [(1, 10), (2, 6), (3, 5), (7, 9)]
print(hi_cal(list_of_tuples))
