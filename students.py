from dataclasses import dataclass

# Original class without the use of dataclasses
# These classes can have methods, but have alot of redundant code.

# class Student:
#     def __init__(self, name, school_id, gpa):
#         self.name = name
#         self.school_id = school_id
#         self.gpa = gpa

#     def __str__(self):
#         return f'Student name: {self.name}, ID: {self.school_id}, GPA: {self.gpa}'



# alex = Student('Alex', 'abcdef', 3.4)
# print(alex)

# sam = Student('Sam', 'qwerty', 4.0)
# print(sam)


#Here we use dataclasses for a more concicely built class
#This class cannot have methods, but is perfect for storing data without alot of extra code needed to be writem

@dataclass
class Student: #Making variables and specifying datatypes
    name: str
    school_id: str
    gpa: float # Added a float for the lab


def main(): # Main program 
    alex = Student('Alex', 'abcdef', 3.4) #Make two students with example data, and print them
    print(alex)

    sam = Student('Sam', 'qwerty', 4.0)
    print(sam)


if __name__ == '__main__': # Call main
    main()