import Student as stu
import Course as cse

s1=stu.Student()
s1.display_student_info()

c1=cse.Course("1233","OOP","CS",3)
c1.display_course_info()

s1.add_course(c1)
s1.display_student_info()