
foodList = ["Kachori","Momo","Pizza","Tension"]
for item in foodList:
  print("Fav food is: ",item)


# create fav food list by for loop

foodList1 = []
n = int(input("How many fav food items do you want to added in this: "))
# range(n) strart 0 step +1
for i in range(n):
   food = input("Enter food name: ")
   foodList1.append(food)

print("Fav food list: ",foodList1)


# until user stop the loop food will be added

foodList2 = []

while True:
   food = input("Enter food name (type 'stop' to finish): ")
   if food.lower() == "stop":
     break
   foodList2.append(food)

print("Fav food list: ",foodList2)     