#피보나치 수열 재귀함수의 문제를 메모화로 해결

memo = {1 : 1, 2 : 1}         #f1, f2는 1로 미리 저장
count = 0
def f(n):
  global count
  count += 1
  if n in memo:
    return memo[n]             #조기리턴
  output = f(n-1) + f(n-2)
  memo[n] = output
  return output


print("{}".format(f(100)))
print("{}번 반복".format(count))   