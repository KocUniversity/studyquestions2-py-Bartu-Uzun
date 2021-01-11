class Animal(object):
  def __init__(self, name):
    self.name = name

class Dog(Animal):
  def __init__(self, name):
    Animal.__init__(self, name)

  def speak(self):
    return self.name + " says WOOF"
            
class Cat(Animal):
  def __init__(self, name):
    Animal.__init__(self, name)
      
  def speak(self):
    return self.name + " says MEOW"


my_dog = Dog("Runner")
my_cat = Cat("Cotton")

print(my_dog.speak())
print(my_cat.speak())

"""It is about inheritance, subclasses and superclasses. Both cat class and
dog class are subclasses of the parent class Animal. Sub classes
inherit their parent classes, meaning that anything their parent class
can do, they can do it as well. However, they might have their own
spesifications, functions, etc.That means a dog cannot use the speak
function implemented under the Cat class, however it can use the
init function under the Animal class, aka its superclass, or parentclass
"""