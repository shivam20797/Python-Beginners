# write a program that prints first n natural numbers

num = int(input("Enter a number: "))
i = 1
while(i<=num):
  print(i)
  i+=1


# write a program that prints sum of first n natural numbers

sum = 0
j = 1
while j<=num:
  sum = j+sum
  j+=1

print("Sum is: ",sum)