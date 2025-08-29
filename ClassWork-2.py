gradeTotal=0
letterGrade=""
grades=input("Enter GradePoints for each course seperated by a comma ',': ").split(",")

for grade in grades:
    gradeTotal+=int(grade)

average=gradeTotal/len(grades)

if average>=90:
    letterGrade="A"
elif average>=80:
    letterGrade="B"
elif average>=70:
    letterGrade="C"
elif average>=60:
    letterGrade="D"
else:
    letterGrade="F"

print("Grade Point total:",gradeTotal)
print("Overall Average: ", average)
print("Letter Grade: ", letterGrade)


