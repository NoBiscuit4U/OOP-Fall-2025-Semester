class Student:
    def __init__(self):
        student_base_info=input("Enter the student info in Format: ID,Name,Major,DoB,GPA: ").split(",")
        self.studentInfo={
            "ID":student_base_info[0],
            "Name": student_base_info[1],
            "Major": student_base_info[2],
            "DoB": student_base_info[3],
            "GPA":student_base_info[4],
            "Courses":[]
        }

    def get_student_info(self,key=""):
        if key in self.studentInfo.keys():
            return self.studentInfo[key]
        else:
            return self.studentInfo

    def edit_student_info(self):
        key=input("Desired Key to Edit: ")
        value=input("Input Value for Key : ")
        self.studentInfo[key]=value

    def add_course(self,course):
        self.studentInfo["Courses"].append(course)

    def display_student_info(self):
        print("Student Info: ")
        for key in self.studentInfo.keys():
            if key == "Courses":
                print("Course Information: ")
                for course in self.studentInfo[key]:
                    course_info=course.get_course_info()
                    print("    Course: "+course_info["Name"])
                    for ckey in course_info.keys():
                        print(f"        {ckey}: ", course_info[ckey])
            else:
                print(f"    {key}: ", self.studentInfo[key])