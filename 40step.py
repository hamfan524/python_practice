#게터세터 -> 프로퍼티 사용

class Rect:
  def __init__(self, width, height):
    if width <= 0 or height <= 0:
      raise Exception("너비와 높이는 음수가 나올 수 없습니다.")

    self.__width = width
    self.__height = height
  @property
  def width(self):
    return self.__width
  @width.setter
  def width(self, width):
    if width <= 0:
      raise Exception("너비는 음수가 나올 수 없습니다.")
    self.__width = width

  @property
  def height(self):
    return self.__height
  @height.setter
  def height(self, height):
    if height <= 0:
      raise Exception("높이는 음수가 나올 수 없습니다.")
    self.__height = height

  def get_area(self):
    return self.__width * self.__height

rect = Rect(1, 1)
rect.width += 10
rect.height = -10
print(rect.get_area())