# 1~100 - 2진수 - 0이 하나만 포함된 숫자 > 합!
output = []                                   #리스트 생성

for i in range(1, 100 + 1):
  if "{:b}".format(i).count("0") == 1:                #2진수로 변환했을때 0의 개수가 1일때 실행
    print("{} : {:b}".format(i, i))
    output.append(i)

print("합계 : ", sum(output))

print()

#리스트 내포를 이용하기
output2 = [i for i in range(1, 100 + 1) if "{:b}".format(i).count("0") == 1]  

for i in output2:
  print("{} : {:b}".format(i, i))
print("합계 : {}".format(sum(output2)))
  