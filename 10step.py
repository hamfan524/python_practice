numbers = [1,2,3,4,5,1,3,7,5,6,2,4,8,9,3,2,4,5]
counter = {}

for number in numbers:
  if number in counter:
    counter[number] += 1

  else:
    counter[number] = 1


print(counter)