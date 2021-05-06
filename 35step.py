# raise = 예외객체

try:
  a = [273, 103, 52, 57, 100]

  number = int(input("정수 입력(0~4까지 입력해주세요)>"))
  print(a[number])

except ValueError as exception:
  print("값에 문제가 있습니다.")
except IndexError as exception:
  print(("0~4까지 입력해주세요."))
except Exception as exception:
  print("알 수 없는 예외가 발생했습니다.")

'''except Exception as exception:
  if type(exception) == ValueError:
    print("값에 문제가 있습니다.")
  elif type(exception) == IndexError:
    print("0~4까지 입력해주세요.") 
  else:
    print("알 수 없는 예외가 발생했습니다.")
    
    '''