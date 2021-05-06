#lambda이용하기

a = list(range(0, 100))
b = filter(lambda number: number % 2 == 0, a)   #필터함수 사용해서 짝수만 필터링하기
print(list(b))


print(list(map(lambda number: number *number , a)))   #map함수 사용해서 제곱 출력

print([i * i for i in a if i % 2 == 0])         #리스트 내포로 제곱 후 짝수만 골라 출력하기

