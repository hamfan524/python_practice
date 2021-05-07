class Student:

  def __init__(self, name, age):
    print("객체가 생성되었습니다.")
    self.name = name
    self.age = age
  def __del__(self):
    print("객체가 소멸되었습니다.")
  def output(self):
    print(self.name, self. age)

student = Student("최동호", 24)
student.output()
