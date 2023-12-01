# Given 6 numbers.
# Remove one and split the other to two groups that the sum of one is double the sum of the other

from itertools import combinations
import sys
numbers = [31, 20, 19, 18, 16, 15]

def split_numbers(numbers):
  for i in range(1, len(numbers)):
    for combo in combinations(numbers, i):
      group1 = set(combo)
      group2 = set(numbers) - group1
      if group1 and group2:
        yield group1, group2

for removed in range(len(numbers)):
  remaining_numbers = numbers[0:removed] + numbers[removed + 1:len(numbers)]

  for group1, group2 in split_numbers(remaining_numbers):
    if sum(group1)*2 == sum(group2) or sum(group2)*2 == sum(group1):
      print(f"The left out number is {numbers[removed]}")
      print("The groups:")
      print(" + ".join([str(n) for n in group1]) + " = " + str(sum(group1)))
      print(" + ".join([str(n) for n in group2]) + " = " + str(sum(group2)))
      sys.exit(0)

print("No result was found")
