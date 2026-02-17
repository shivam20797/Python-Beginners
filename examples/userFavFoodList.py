food1 = input("Enter food 1:")
food2 = input("Enter food 2:")
food3 = input("Enter food 3:")

# 1 way
foodList = [food1,food2,food3]
print(foodList)

# 2 way
foodListNew = []
foodListNew.append(food1)
foodListNew.append(food2)
foodListNew.append(food3)
print(len(foodListNew))
print(foodListNew)