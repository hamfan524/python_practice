#재귀함수로 리스트를 평탄화하는 함수 만들어보기
#리스트 평탄화는 중첩된 리스트가 있을 시 중첩 제거 - 1차원 리스트로 만드는것

def flatten(data):
  output = []
  for i in data:
    if type(i) == list:
      output += flatten(i)
    else:   
      output += [i]     #output.append(i)
  return output

example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print("원본 : ", example)
print("변환 : ", flatten(example))