key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
character = {}

for i in range(len(key_list)):
  character[key_list[i]] = value_list[i]

print(character)

# character출력 : {'name': '기사', 'hp': 200, 'mp': 30, 'level': 5} 만들기