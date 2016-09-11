from random import shuffle

def highest_product(numbers):
  if len(numbers) < 3:
    return "Need at least three numbers"

  # Now we need to keep of two types, the smallest product of two(potentially negative), and the largest product of two, and of course
  # the highest product of three

  first = numbers.pop(0)
  second = numbers.pop(0)
  third = numbers.pop(0)

  maximum_product_of_three = first * second * third
  minimum_product_of_two = min(first * second, first * third, second * third)
  maximum_product_of_two = max(first * second, first * third, second * third)
  minimum = min(first, second, third)
  maximum = max(first, second, third)

  while(len(numbers) > 0):
    number = numbers.pop(0)

    maximum_product_of_three = max(maximum_product_of_three, minimum_product_of_two * number, maximum_product_of_two * number)

    minimum_product_of_two = min(minimum_product_of_two, maximum * number, minimum * number)

    maximum_product_of_two = max(maximum_product_of_two, maximum * number, minimum * number)

    minimum = min(minimum, number)
    maximum = max(maximum, number)


  return maximum_product_of_three

numbers = [1,2,3,4,5,6,7, -10, -5]
shuffle(numbers)
print(numbers)
print(highest_product(numbers))
