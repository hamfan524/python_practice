class Student:

  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __eq__(self, other):
    return self.age == other.age and \
      (self.name == other.name)
  def __ne__(self, other):
    return self.age != other.age
  def __gt__(self, other):
    return self.age > other.age
  def __ge__(self, other):
    return self.age >= other.age
  def __lt__(self, other):
    return self.age < other.age
  def __le__(self, other):
    return self.age <= other.age


student = Student("최동호", 24)
student2 = Student("배재흥", 25)

print(student == student2)
print(student != student2)
print(student > student2)
print(student >= student2)
print(student < student2)
print(student <= student2)