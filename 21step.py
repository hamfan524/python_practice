#*가변매개변수는 함수 1개에 1개만 허용, 무조건 마지막에 들어가야함
#기본매개변수 뒤에는 일반적인 매개변수가 오지 못함
def print_n_times(value, n = 5):
  for i in range(n):
    print(value)


print_n_times("안녕하세요")