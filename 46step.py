from urllib import request
from bs4 import BeautifulSoup

content = request.urlopen("http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=2629057000")
soup = BeautifulSoup(content, 'html.parser')

for data in soup.select("data"):
  print("시간 : ", data.select_one("hour").string)
  print("날씨 : ", data.select_one("wfKor").string)
  print("-" * 20)