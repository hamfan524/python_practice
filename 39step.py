#게터세터 사용 -> 개떡같음 ㅠ

class Rect:
  def __init__(self, width, height):
    if width <= 0 or height <= 0:
      raise Exception("너비와 높이는 음수가 나올 수 없습니다.")

    self.__width = width
    self.__height = height

  def get_width(self):
    return self.__width
  def set_width(self, width):
    if width <= 0:
      raise Exception("너비는 음수가 나올 수 없습니다.")
    self.__width = width

  def get_height(self):
    return self.__height
  def set_height(self, height):
    if height <= 0:
      raise Exception("높이는 음수가 나올 수 없습니다.")
    self.__height = height

  def get_area(self):
    return self.__width * self.__height

rect = Rect(1, 1)
rect.set_width(rect.get_width() + 10)
rect.set_height(rect.get_height() + 10)
print(rect.get_area())