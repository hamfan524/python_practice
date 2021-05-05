dictionary = {
  "이름": "구름",
  "종족": "강아지"
}

print(dictionary.get("이름"))
print(dictionary["이름"])

if dictionary.get("나이") == None:
  print("없는키입니다.")
else:
  print(dictionary.get("나이"))
