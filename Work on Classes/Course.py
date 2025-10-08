class Course:
    def __init__(self,id,name,deprtmnt,credhrs):
        self.courseInfo = {
            "ID": id,
            "Name": name,
            "Department": deprtmnt,
            "Credit Hrs": credhrs,
        }

    def get_course_info(self,key=""):
        if key in self.courseInfo.keys():
            return self.courseInfo[key]
        else:
            return self.courseInfo

    def display_course_info(self, key=""):
        print("Course Information: ")
        if key in self.courseInfo.keys():
            print(f"{key}: ",self.courseInfo[key])