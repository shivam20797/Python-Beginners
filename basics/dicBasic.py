# Dictory Basic

student = {
  "name" : "Shivam",
  "age" : 25,
  "city" :  "jaipur",
}

print(type(student))
print(len(student))
print(student["name"])

# update city

student["city"] = "Mumbai"
student["stream"] = "cs"
print(student)

# remove
student.pop("stream")
print(student)