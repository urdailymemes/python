numbers = [24, 45, 16, 77, 48, 19, 10]
maximum = numbers[0]
for num in numbers:
  if num > maximum:
    maximum = num
print('max =', maximum)