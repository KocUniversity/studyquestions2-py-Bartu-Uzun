# Inheritance Q1

def read_file():
  # TODO: extract name, ID, and the score from the file
  f = open('input.txt', 'r')
  data = f.readlines()
  print(data)
  name = data[0].split()
  print(name)
  ID = data[1].split()
  print(ID)
  scores = data[2].split()
  

  r_dict = {'name' : name, 'ID': ID, 'scores' : scores}

  return r_dict


class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber

	def __str__(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Player(Person):
  '''
  The __init__ method
    firstName - A string denoting the Person's first name.  
    lastName - A string denoting the Person's last name.
    id - An integer denoting the Person's ID number.
    scores - An array of integers denoting the Person's test scores.
  '''
  def __init__(self, firstName, lastName, idNumber, scores):
    Person.__init__(self, firstName, lastName, idNumber)
    self.scores = scores


  '''
  The calculate method
    Returns one of the characters A, B, C, D 
    denoting the grade of the player.
  '''
  def Calculate(self):
    total = 0
    for score in self.scores:
      total += int(score)
    avg = total / len(self.scores)
    if avg >= 20:
      grade = 'A'
    elif 20 > avg >= 15:
      grade = 'B'
    elif 15 > avg >= 5:
      grade = 'C'
    else:
      grade = 'D'
    return grade


  '''
  The total_matches method
    Returns how many matches are played by the player.
  '''
  def total_matches(self):
    return len(self.scores)

  


player_dict = read_file()

print(player_dict)
# TODO: create the Player instance, print it
p1 = Player(player_dict['name'][0], player_dict['name'][1], player_dict['ID'][0], player_dict['scores'] )
# TODO: compute the grade of the player and print it
grade = p1.Calculate()
print(grade)

print(p1.firstName)

print(p1.idNumber)

