class Student:
   'Common base class for all Students'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Student.empCount += 1
   
   def displayCount(self):
     print("Total Student %d" % Student.empCount)

   def displayStudent(self):
      print( "Name : ", self.name,  ", Salary: ", self.salary)

"This would create first object of Student class"
emp1 = Student("Zara", 3000)
"This would create second object of Student class"
emp2 = Student("Manni", 5000)
emp1.displayStudent()
emp2.displayStudent()
print("Total Student %d" % emp1.empCount)