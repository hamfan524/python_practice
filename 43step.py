#백준 10871번 문제 정답

n, x = map(int, (input().split()))
a = list(map(int, (input().split())))

'''
for i in range(n):
   if a[i] < x:
      b = a[i]
      print(b, end=" ")
      '''

b = [a[i] for i in range(n) if a[i] < x]
for j in b:
   print(j, end=" ")