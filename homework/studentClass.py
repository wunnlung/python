#the code at the bottom is what the code uses to create new student objects
#(its inside the main)
#the initialize variableas for students are student name, student id,
#and their course list
#for any student you create, you can set their course list, add a course.
#print all of their info, and change their name (im assuming for nicknames?)
#added the getID func to return the id for a specific student


#program to create a class called Student and a main program that will test it        
class Student:
    """This class has the following instance variables.
            name: a string holding the student's last name,
            id: a unique integer identifying the student
            courseList: a list of strings, each string representing
                a course the student is enrolled in"""

    def __init__(self, studName, studID, studCourseList=[]):
        """Constructor - takes name, id, and courseList -
            default for courseList is the empty list"""
        self.name=studName
        self.id=studID
        self.courseList=studCourseList

    def getID(self):
        return self.id

    def setCourseList(self, newList):
        """changes courseList to the new list of courses"""
        self.courseList=newList

    def addCourse(self, name):
        """adds a course to the list"""
        self.courseList.append(name)
        
    def printInfo(self):
        """prints out student information"""
        print('------------')
        print ("Courses for " + self.name + " (ID# " + str(self.id) + "): ")
        print('------------')
        if self.courseList!=[]:
            for course in self.courseList:
                print(course)
        else:
            print("No courses for " + self.name)

    def changeName(self, newName):
        """changes name to the newName"""
        self.name = newName

def main2():
    #create a student
    #this creates a student
    stu1=Student('Jones',89765,['COM110', 'HIS112','DAN100'])
    stu1.addCourse('HIS101')
    stu1.printInfo()
    #create another student
    stu2=Student('Gonzalez',65432)
    stu2.printInfo()
    stu2.setCourseList(['MAT112','BIO207','PSY122'])
    stu2.printInfo()
    stu2.changeName("Martinez")
    stu2.printInfo()


if __name__ =='__main__':
    main2()
