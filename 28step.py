file = open("test.txt","w")
file.write("안녕하세요.")
file.close()                      #파일 오픈 후 클로즈

with open("test.txt","r") as file:
  print(file.read())              #with를 사용해서 자동으로 닫기

'''
어떤 대상
-텍스트파일:텍스트 에디터로 열 수 있어
-바이너리 파일:텍스트 에디터로 열 수 없어(이미지, 동영상, 워드, 엑셀, PDF 등)

어떻게 다룰것인가

-쓰기
  -완전히 새로 쓰기(write) : w
  -있는 파일 뒤에(append) : a
-읽기(read) : r
'''
