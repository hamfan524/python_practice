
a = [273, 103, 52, 32, 57]

print(list(enumerate(a)))                        # - enumerate함수는 일회용 함수 = 제너레이터

for i,element in enumerate(a):
  print("{}번째 요소는 {}입니다.".format(i, element))
  
  
  
b = {
  "key_1": "value_1",
  "key_2": "value_2",
  "key_3": "value_3"
}

for key, value in b.items():
  print("{}의 값은 {}입니다.".format(key, value))   #딕셔너리에서 items함수 사용

