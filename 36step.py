def new_student(name, korean, math, english, science):
  return{
    "name": name,
    "korean": korean,
    "math": math,
    "english": english,
    "science": science
  }
  
def sum(student):                     #총점 구하는 함수 
  return student["korean"] + student["math"] +\
    student["english"] + student["science"]
def average(student):                 #평균 구하는 함수
  return sum(student) / 4
def output(student):                  #출력하는 함수
  print(student["name"], sum(student), average(student), sep="\t")


# ------------------------------------------ #
# 학생 리스트를 선언합니다.

students = [
  new_student("윤인성", 87, 98, 88, 95),
  new_student("연하진", 92, 98, 96, 98),
  new_student("구지연", 76, 96, 94, 90),
  new_student("나석주", 98, 92, 96, 92),
  new_student("윤아린", 95, 98, 98, 98),
  new_student("윤명월", 64, 88, 92, 92)
]
# 학생을 한 명씩 반복합니다.
print("이름", "총점", "평균", sep="\t")
for student in students:
  output(student)