class Polygon:
  def __init__(self, no_of_sides):
    self.n = no_of_sides
    self.sides = [0 for i in range(no_of_sides)]

  def inputSides(self):
    # TODO
    for i in range(self.n):
      side_no = i + 1
      self.sides[i] = float(input("Enter side {} :".format(side_no)))

  def dispSides(self):
    # TODO
    for i, side in enumerate(self.sides):
      print("Side", (i + 1), 'is', side)

class Triangle(Polygon):
  def __init__(self):
    Polygon.__init__(self, 3)

  def findArea(self):
    # TODO
    o = 0
    for side in self.sides:
      o += side
    u = o / 2
    area = (u * (u - self.sides[0]) * (u - self.sides[1]) * (u - self.sides[2])) ** (1 / 2)
    print("The area of the triangle is", area)


t = Triangle()
t.inputSides()
t.dispSides()
t.findArea()
