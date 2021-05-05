max = 0
n = 0
max_i = 0
max_j = 0

for i in range(1, 100, 1):
  n = i * (100 - i)
  if max < n:
    max = n
    max_i = i
    max_j = (100 - i)
    
print("최대가 되는 경우 : {} * {} = {}".format(max_i, max_j, max))
