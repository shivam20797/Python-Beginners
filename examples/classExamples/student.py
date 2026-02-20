class Student:
  name = "guest"
  def __init__(self,name):
    self.name = name

  def hello(self):  # methods
    print("Hello", self.name)  


s1 = Student("Shivam")
s2 = Student("Aakash")

print("Stundent1 name:",s1.name)
s1.hello()
print("Stundent2 name:",s2.name)