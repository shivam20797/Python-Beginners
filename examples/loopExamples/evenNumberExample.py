# write a program to print all even number between 1 to 50 using a while loop:

num = 1
while num <= 50:
  if num %2 == 0:
    print("Even number is: ",num)
  num+=1
print("\nEnded here \n ")

# write a program to print all even number between 1 to 50 using a for loop and range:

for item in range(1,51):
  if item%2 ==0:
    print("Even number is: ",item)

print("\nEnded here \n ")


for item in range(2,51,2):
  if item%2 ==0:
    print("Even number is: ",item)