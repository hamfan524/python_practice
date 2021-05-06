numbers = [ 1, 2, 3, 4, 5, 6]

print("::".join(
  map(str, numbers)            
))              #numbers안에 int형이기 때문에 모두 str로 바꿔주려면 map으로 새로운 리스트 생성

#실행결과 - 1::2::3::4::5::6



number = list(range(1, 10 + 1))

print("#홀수만 출력하기")
print(list(filter(lambda a: a % 2 == 1, number)))
print()

print("#3 이상, 7 미만 출력하기")
print(list(filter(lambda a: 3 <= a < 7, number)))
print()

print("#제곱해서 50 미만 추출하기")
print(list(filter(lambda a: a ** 2 < 50, number)))
