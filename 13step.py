number = [ 1, 2, 1, 2, 1, 2, 1, 2]

while 1 in number:
  number.remove(1)
  print(number)                               # - while문으로 리스트 내의 1 제거하기

import time

first = time.time()
while first + 3 > time.time():
  pass                                        # - time함수와 while문으로 3초 뒤 종료되는 프로그램

print("프로그램이 종료되었습니다.")