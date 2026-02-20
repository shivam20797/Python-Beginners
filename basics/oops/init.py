class Vehicle:
  name = "car"
  def __init__(self,name):
    self.name = name
    print('Called in new object',self,self.name)



v1 = Vehicle("Bike")
print(v1)
v2 = Vehicle("Car")