import sys
# for coloring CMD / PowerShell in non-ANSI environment
# conda install -c anaconda colorama
import colorama
colorama.init()

yes = {'yes','y', 'ye', ''}
no = {'no','n'}

# without colorama -> Requires ANSI capable console
colorChoice = input("Do you want to use console colors? [y/n]: ").lower()
if colorChoice in yes:
    class bcolors:
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        ENDC = '\033[0m'

else:
    class bcolors:
        OKBLUE = ''
        OKGREEN = ''
        ENDC = ''

###########
# classes #
###########

class Register:
    def __init__(self, className:str):
        self.students = []
        self.className = className
    def __str__(self):
        out = f"{bcolors.OKGREEN}" + str(self.className) + f"{bcolors.ENDC}\n"
        for num, i in enumerate(self.students, start=1):
            out += str(num) + ". " + str(i)
        return out
    def addStudent(self, name, surname):
        self.students.append(Student(name, surname))
        return self.students[-1]
    def sort(self):
        self.students = sorted(self.students)
        return self

    # find student by surname, full name, or full name in 2 arguments
    # returns first matching object
    # possible mixup when multiple people have the same name
    def find(self, name, lastName=None):
        name = name.split(" ")
        firstName = name[0]
        if(lastName):
            return next((x for x in self.students if x.firstName == firstName and x.lastName == lastName), None)
        if(len(name) > 1):
            lastName = name[1]
            return next((x for x in self.students if x.firstName == firstName and x.lastName == lastName), None)
        lastName = name[0]
        return next((x for x in self.students if x.lastName == lastName), None)

    # list students that have at least one mark in specific course
    # should return list of students instead of string
    def listCourse(self, course:str):
        out = f"{bcolors.OKGREEN}" + str(course) + f"{bcolors.ENDC}\n"
        index = 1
        for i in self.students:
            if(course in i.marks):
                out += str(index) + ". " + str(i.fullName) + f"{bcolors.OKBLUE} " + str(i.marks[course]) + f"{bcolors.ENDC}\n"
                index += 1
        return out

class Student:
    def __init__(self, firstName:str, lastName:str):
        self.marks = dict()
        self.firstName = firstName
        self.lastName = lastName
        self.fullName = firstName + " " + lastName
    def __str__(self):
        return str(self.fullName) + f"{bcolors.OKBLUE} " + str(self.marks) + f"{bcolors.ENDC}\n"
    def __repr__(self):
        return str(self)
    def __lt__(self, other):
        return ((self.lastName, self.firstName) < (other.lastName, other.firstName))
    def addMark(self, mark:int, course:str):
        if(course in self.marks):
            self.marks[course] += (mark,)
        else:
            self.marks[course] = (mark,)
        return self

########
# main #
########

if __name__ == "__main__":
    register = Register("class 1A")

    register.addStudent("Piotr", "Kolecki").addMark(5, "Math")
    register.addStudent("Janusz", "Gajos")
    register.addStudent("Adam", "Abacki")
    register.addStudent("Barbara", "Babacka")
    register.addStudent("Cecylia", "Cecacka")

    print(register)

    register.sort()

    print(register)

    register.find("Kolecki").addMark(1, "IT").addMark(2, "IT").addMark(3, "IT").addMark(4, "IT").addMark(5, "IT")
    register.find("Janusz Gajos").addMark(1, "Math").addMark(2, "Math").addMark(3, "Math").addMark(4, "Math").addMark(5, "Math")
    register.find("Adam", "Abacki").addMark(1, "Science").addMark(2, "Science").addMark(3, "Science").addMark(4, "PE").addMark(5, "PE")
    
    print(register.find("Kolecki"))
    print(register.find("Janusz Gajos"))
    print(register.find("Adam", "Abacki"))

    print(register.listCourse("Math"))

    print(register)
