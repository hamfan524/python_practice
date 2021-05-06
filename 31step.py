# 숫자를 입력받습니다.

while True:
  string_input = input("정수 입력 > ")
  if string_input.isdigit():          #정수일때 실행 후 break
    number_input_a = int(string_input)
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
    break
  else:                               #정수가 아닐 시 계속 반복
    print("정수를 입력해주세요!")