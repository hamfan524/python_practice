import datetime

now = datetime.datetime.now()

if now.hour < 12:
  print("현재 시간은 {}시 {}분으로 오전입니다!".format(now.hour, now.minute))

elif now.hour == 12 :
  print("현재 시간은 {}시 {}분으로 정오입니다!".format(now.hour, now.minute))

else :
  print("현재 시간은 {}시 {}분으로 오후입니다!".format(now.hour, now.minute))

# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)