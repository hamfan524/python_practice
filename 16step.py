limit = 10000

i = 1
sum_value = 0

while sum_value < limit:
  sum_value += i
  i += 1                                  # for반복문은 몇번 반복하는지 예상이 가능할 때 써주는게 낫다

print("{}를 더할 때 {}을 넘으며 그때의 값은 {}입니다.".format(i, limit, sum_value))

# 출력 : 142를 더할 때 10000을 넘으며 그때의 값은 10011입니다.