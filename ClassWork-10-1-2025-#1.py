class student:
    def __init__(self):
        student_base_info=input("Enter the student info in Format: ID,Name,Major,DateofBirth,GPA: ").split(",")
        self.studentInfo={
            "ID":student_base_info[0],
            "Name": student_base_info[1],
            "Major": student_base_info[2],
            "DOB": student_base_info[3],
            "GPA":student_base_info[4],
            "CurrentCourses":[]
        }

    def get_student_info(self,key=""):
        if key in self.studentInfo.keys():
            return self.studentInfo[key]
        else:
            return self.studentInfo

    def edit_student_info(self,key):
        value=input("Input Value for "+key+" : ")
        self.studentInfo[key]=value

    #def display_student_info(self):
     #   for key in self.studentInfo.keys():
