# function basic

def sumfun() :
  a = 10
  b = 20
  return a+b

print(sumfun())

# argument function

def averagefun(a,b) :
  return (a+b)//2


# default argument function

def greet(name = "Guest") :
  return name


print("Hello",greet("Ravi"))
print("Hello",greet())
