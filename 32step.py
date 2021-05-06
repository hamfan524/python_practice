while True:
  try:
      # 예외가 발생할 수 있는 가능성이 있는 코드
      print(float(input(">숫자를 입력해주세요: ")) ** 2)
      break
  except:
      # 예외가 발생했을 때 실행할 코드
      pass
