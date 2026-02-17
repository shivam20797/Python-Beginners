# create a dictionary  name marks to store marks of 3 subjects.
# add the subject one by one and print the final dictionary

print("Enter subject and marks:\n")
marks = {}
subjectName = input("Enter subject name1 ")
subjectMarks= int(input("Enter subject marks1: "))
subjectName1 = input("Enter subject name2: ")
subjectMarks1= int(input("Enter subject marks2: "))
subjectName2 = input("Enter subject name3: ")
subjectMarks2 = int(input("Enter subject marks3: "))
marks[subjectName] = subjectMarks
marks[subjectName1] = subjectMarks1
marks[subjectName2] = subjectMarks2
print(marks)