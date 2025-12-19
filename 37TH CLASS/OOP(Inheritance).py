class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname,self.lastname)

class SchoolInfo:
     def __init__(self,school_name):
          self.schoolName=school_name

class student(person,SchoolInfo):
    def __init__(self,fname,lname,year,school_name):
        person.__init__(self,fname,lname)
        SchoolInfo.__init__(self,school_name)
        self.GraduationYear=year
    def Welcome(self):
            print("Welcome",self.firstname,self.lastname," You graduated in year ",self.GraduationYear,"from",self.schoolName)

class CollegeStudent(student):
    def __init__(self, fname, lname, year, school_name, major):
        super().__init__(fname, lname, year, school_name)
        self.major = major

obj=student("Ali","Raza","2027","QBHHSS","Adamjee")
obj.printname()
obj.Welcome()