foodList = ["chole bathure","choco waffle","kachori","jalebi"]

#length of lst
print("Length of list",len(foodList))

#indexing
print("Item in list",foodList[0])

#replace value
print("list",foodList)
foodList[3] = "change" 
# list are mutable and string are immutable
print("Updated list",foodList)

#slicing

print("Item in list",foodList[1:4])
print("Item in list",foodList[:4])
print("Item in list",foodList[:-4])


# function of list
foodList.pop(3)
print(foodList)

foodList.append("Test")
print(foodList)

foodList.sort()
print(foodList)


foodList.remove("Test")
print(foodList)