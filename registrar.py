#module to create a Registrar Class
#imports the Student class from module StudentClass.py

from studentClass import *

class Registrar:
    """class Registrar has the following instance variables:
        studentList is a list of Student objects
        totStudents is an integer that counts the total number of students"""

    def __init__(self):
        """constructor sets up a blank registrar"""
        self.studentList=[] 
        self.totStudents=0;
        
    def addStudent(self, stu):
        """add a new student (Student object stu) to the Registrar"""
        self.studentList.append(stu)
        self.totStudents = self.totStudents + 1

    def deleteStudent(self, stu):
        """delete a student (Student object stu) from the list"""        
        for student in self.studentList:
            if student==stu:
                self.studentList.remove(stu)
                self.totStudents = self.totStudents - 1

    def printInfo(self):
        """print out the information for all students"""
        print ('++++++++++++++')
        print ("There are " + str(self.totStudents) + " students currently registered." )
        for student in self.studentList:
            student.printInfo()
        print ('++++++++++++++')

    def registerCourse(self, stuID, courseName):
        for i in self.studentList:
            if stuID == i.getID():
                i.addCourse(courseName)
                print("course added")
                #return none so it doesn't loop through the rest of the list
                #we want to end the program when it adds a course
                return None
        print("no student was found with that ID")



#Test out our registrar class
def main2():

    #create two students
    student1 = Student("Jones", 23423, ["COM110","BIO101", "PSY101"])
    student2 = Student("Gonzalez", 65234)
    #creates a registrar
    r = Registrar()
    #adds the two students
    r.addStudent(student1)
    r.addStudent(student2)
    #runs get info
    r.printInfo()
    #add a course to a valid student
    r.registerCourse(23423, "Biology")
    #get the info with the added course
    r.printInfo()
    #try to add a course to a non valid student
    r.registerCourse(10101, "Null Class hehe")


main2()
