class Student:
  studentName  = "Guest"
  marksList = []
  def __init__(self,studentName,marksList,subjectList):
    self.studentName = studentName
    self.subjectList = subjectList
    self.marksList = marksList

# instance method
  def averageMarks(self):
    sum = 0
    for mark in self.marksList:
      sum = sum + mark
    print("Average marks: ",sum/len(self.marksList))

# static method
  @staticmethod
  def helloMethod():
    return Student.studentName
    


s1 = Student("Shivam",[90,98,99],["Math","English","Science"])
s1.averageMarks()
print("Hello..",s1.helloMethod())

    
