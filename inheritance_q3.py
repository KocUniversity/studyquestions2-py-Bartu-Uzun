# Inheritance Q3

class A(object):
  def one(self):
    return 'A'

  def two(self):
    return 'B'
 
class B(A):
  def two(self):
    return self.one()

obj1 = A()
obj2 = B()

print(obj1.two(), obj2.two())

## output is B A

## obj1 works fine so no explanation for it, obj2 works because even though one() was not defined under class B, since it is a subclass of class A it will use class A's function one(), returning the string 'A'