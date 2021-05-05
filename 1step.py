year = int(input("태어난 년도를 입력하세요 : "))
year2 = year % 12

tti = "원숭이, 닭, 개, 돼지, 쥐, 소, 호랑이, 토끼, 용, 뱀, 말, 양".split(", ")

print(year,"년에 태어났다면 ", tti[year2],"띠입니다.")

print("{}년에 태어났다면 {}띠입니다.".format(year, tti[year2]))