# Given 6 numbers.
# Remove one and split the other to two groups that the sum of one is double the sum of the other

import sys
import random

max_number_of_tries = 1000000
range_of_numbers = 1000
count_of_numbers = 40

numbers = []
for i in range(count_of_numbers):
  numbers.append(random.randint(1,range_of_numbers))

sum_of_numbers = sum(numbers)

for a_try in range(max_number_of_tries):
  index_left_out = random.randint(0, count_of_numbers-1)
  remaining_numbers = numbers[0:index_left_out] + numbers[index_left_out+1:count_of_numbers]
  sum_of_remaining_numbers = sum_of_numbers - numbers[index_left_out]
  count_1st_group = random.randint(1, count_of_numbers-2)
  count_2nd_group = count_of_numbers - count_1st_group

  # choose 1st group
  group1 = random.sample(remaining_numbers, count_1st_group)
  sum_of_group1 = sum(group1)
  sum_of_group2 = sum_of_remaining_numbers - sum_of_group1

  if sum_of_group1*2 == sum_of_group2 or sum_of_group2*2 == sum_of_group1:
    group2 = set(remaining_numbers) - set(group1)
    print(f"The left out number is {numbers[index_left_out]}")
    print("The groups:")
    print(" + ".join([str(n) for n in group1]) + " = " + str(sum(group1)))
    print(" + ".join([str(n) for n in group2]) + " = " + str(sum(group2)))
    print(f"Took {a_try+1} iterations.")
    sys.exit(0)

print("No result was found")
