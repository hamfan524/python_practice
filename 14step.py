
i = 0

while True:
  print("{}번째 반복문입니다.".format(i))
  i += 1

  input_text = input("> 종료하시겠습니까?(y)")
  if input_text in ["Y", "y"]: # = if input_text.lower() == "y":
    print("반복을 종료합니다.")
    break                                 #반복문 벗어나기


numbers = [5, 15, 6, 20, 7, 25]

for number in numbers:
  if number < 10:
    continue                              #현재 반복을 중지하고, 다음 반복으로 넘어간다 들여쓰기를 안써도 된다는 장점이 있음
  print(number)                           #pass랑 else를 쓰거나 부호만 바꿔줘도 똑같지만 python에선 자주쓴다.
