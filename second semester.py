'''class Cat: # This is a class definition for a Cat, class is a blueprint for creating objects
    def __init__(self, name, color= "black"): # This is the constructor method that initializes the Cat object
        self.name = name # This initializes the name attribute of the Cat object
        self.age = 2 # This initializes the age attribute of the Cat object
        self.color = color # This initializes the color attribute of the Cat object

cat1 = Cat("Tom") # This creates an instance of the Cat class with the name "Tom"
cat2 = Cat("Jerry" "white") # This creates another instance of the Cat class with the name "Jerry"

print(cat1.name, "is", cat1.age,"years old and is", cat1.color)  # Output: Tom is 2 years old and is black'''

class ComputerscienceB:
    def __init__(self, name, age, grade=40):
        self.name = name
        self.age = age
        self.grade = grade
    def set_compliment(self, compliment):
        self.compliment = compliment

Student1 = ComputerscienceB("Luara Froes", 24, 70)
Student2 = ComputerscienceB("Manar Ed", 21, 75)
Student3 = ComputerscienceB("Felix", 34)
Student1.set_compliment("she is amazing!")  # this will set the complement of the student 1 to "she is amazing!"

print("\n" "printing the information of the students")
print (Student1.name, "is", Student1.age, "years old and has a grade of", Student1.grade, Student1.compliment, )  # it will print the name, age and grade of the student 1 and the complement
print (Student2.name, "is", Student2.age, "years old and has a grade of", Student2.grade)  # it will print the name, age and grade of the student 2
print (Student3.name, "is", Student3.age, "years old and has a grade of", Student3.grade)  # it will print the name, age and grade of the student 3

print("\n" "now in a dictionary")
print(Student1.__dict__)
print(Student2.__dict__)
print(Student3.__dict__)

print("\n" "now in a list and a for loop")

StudentsOfComputerscienceB = [Student1, Student2, Student3]  # this will create a list of the students of the class ComputerscienceB
for student in StudentsOfComputerscienceB:  # this will iterate through the list of students
    print( student.name, "is", student.age, "years old and has a grade of", student.grade )  # it will print the name, age and grade of each student in the lis