# take input as food name get last 2 char and middle  3 char
foodName = input("Enter fav food : ")
midIndex = len(foodName)//2
middle3Char = foodName[midIndex-1:midIndex+2]
last2Char = foodName[len(foodName)-2:len(foodName)]
print("Last 2 char is : ",last2Char)
print("Middle 3 char is : ",middle3Char)