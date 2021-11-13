separator = ('_'* 40+"nowy kod"+'_'* 40)

 #TODO:GENERATORY


def generator_1():
    yield  1,2,3,\
           485

for num in generator_1():
 print(num)
print(separator)

def generator_2():
    yield 1
    yield 2
    yield 3
for num in generator_2():
 print(num)
print(separator)

def generator_3():
 print("linia 1")
 yield 1
 print("linia 2")
 yield 2
 print("linia 3")
 yield 3
 print("koniec")

for num in generator_3():
 print(num)
print(separator)

#TODO:Rzutowanie klas na znane typy prymitywne:

# class Student:
#  def __init__(self, firstname, lastname, year=1, group="A"):
#   self.firstname = firstname
#   self.lastname = lastname
#   self.year = year
#   self.group = group
#
#  def name(self):
#   return "{} {}".format(self.firstname, self.lastname)
#
# s1 = Student("Adam", "Abacki")
# s2 = Student("Bartosz", "Babacki")
# print(s1.name())
# print(s2.name())

class Student:
 def __init__(self, firstname, lastname, year=1, group="A"):
  self.firstname = firstname
  self.lastname = lastname
  self.year = year
  self.group = group

 def __str__(self):
  return "{} {}".format(self.firstname, self.lastname)

 def __int__(self):
  return self.year

 def __float__(self):
  return float(self.year)

 def __bool__(self):
  return self.year > 1


s1 = Student("Adam", "Abacki")
s2 = Student("Bartosz", "Babacki")
print(str(s2))
if s2:
 print("{} nie jest już w pierwszej klasie")

 print(separator)

def __iter__(self):
    yield x
for liczby in range(6):
   print(liczby)




print(separator)

def __iter__(self):
   return iter([0, 1, 2, 3, 4 ,5])
for elem in obj:
   print(elem)