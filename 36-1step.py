#클래스 사용

class student:
  def __init__(self, name, korean, math, english, science):
    self.name = name
    self.korean = korean
    self.math = math
    self.english = english
    self.science = science     
  def sum(self):                     #총점 구하는 함수 
    return self.korean + self.math +\
      self.english + self.science
  def average(self):                 #평균 구하는 함수
    return self.sum() / 4
  def output(self):                  #출력하는 함수
    print(self.name, self.sum(), self.average(), sep="\t")

# ------------------------------------------ #
# 학생 리스트를 선언합니다.

students = [
  student("윤인성", 87, 98, 88, 95),
  student("연하진", 92, 98, 96, 98),
  student("구지연", 76, 96, 94, 90),
  student("나석주", 98, 92, 96, 92),
  student("윤아린", 95, 98, 98, 98),
  student("윤명월", 64, 88, 92, 92)
]
# 학생을 한 명씩 반복합니다.
print("이름", "총점", "평균", sep="\t")
for student in students:
  student.output()