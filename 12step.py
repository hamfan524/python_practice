array = [273, 52, 103, 32, 57]

i = 0

for element in array:
  print("{} : {}".format(i, element))
  i +=  1
print()                               #반복문

for i, element in enumerate(array):
 print("{} : {}".format(i, element))
print()                               #enumerate함수 사용

for i in range(9, 0 - 1, -1):
  print(i)
print()                               #역으로 출력

for i in reversed(range(0, 10)):
  print(i)                            #역으로 출력 - reversed함수 사용
  
for i in reversed(range(len(array))):
  print("{} : {}".format(i, array[i]))
print()                               #len함수와 reversed함수 사용