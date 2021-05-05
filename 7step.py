딕셔너리 = {
  "문자열": "값",
  273: "배재흥 민주당",
  True: False
}

for key in 딕셔너리:
  print("{} : {}".format(key, 딕셔너리[key]))

딕셔너리["키"] = "값"
print()
for key in 딕셔너리:
  print("{} : {}".format(key, 딕셔너리[key]))


del 딕셔너리["키"]
print()
for key in 딕셔너리:
  print("{} : {}".format(key, 딕셔너리[key]))


