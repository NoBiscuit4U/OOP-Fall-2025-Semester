studentName=input("Enter your Name: ")
gradeTotal=0

grades=input("Enter GradePoints for each course seperated by a comma ',': ").split(",")

for grade in grades:
    gradeTotal+=int(grade)

print("Grade Point total for "+studentName+":",gradeTotal)
print("Overall Average: ", gradeTotal/len(grades))