from urllib import request

target = request.urlopen("http://naver.com")
content = target.read()

print(content[:100])