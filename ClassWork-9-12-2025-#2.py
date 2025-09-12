options=["Add Student","Remove Student","Replace Student","Sort By Age List","Display List","Quit"]
student_names=[]
student_ages=[]
student_name=""

while True:
    print("-------")
    print("Options")
    for i in range(0, len(options)):
        print(i," "+options[i])

    selection=int(input("Enter Desired Option: "))

    if selection>0 and selection <3:
        student_name = input("Enter Students Name: ")

    if selection == 0:
        student_info = input("Enter Student Name and Age seperated by a comma: ").split(",")
        student_names.append(student_info[0])
        student_ages.append(student_info[1])
    elif selection == 1:
        for i in range(0,len(student_names)):
            if student_names[i]==student_name:
                student_names.pop(i)
                student_ages.pop(i)
    elif selection == 2:
        student_info = input("Enter Replacement Student Name and Age seperated by a comma: ").split(",")
        for i in range(0,len(student_names)):
            if student_names[i]==student_name:
                student_names[i]=student_info[0]
                student_ages[i]=student_info[1]
    elif selection == 3:
        #No worky :(
        newList=[]
        excluded_indexes=[]
        greater_index=0
        for i in range(0,len(student_ages)):
            greater_value=0
            if i not in excluded_indexes:
                for j in range(0,len(student_ages)):
                    if j not in excluded_indexes:
                        if int(student_ages[i]) > int(student_ages[j]):
                            greater_value = int(student_ages[i])
                            greater_index = i
                        elif int(student_ages[i]) < int(student_ages[j]):
                            greater_value = int(student_ages[j])
                            greater_index = j
                        print("Greater Value", greater_value)
                    excluded_indexes.append(greater_index)
                    newList.append(greater_value)
        print(newList)

    elif selection == 4:
        print("Student Names: ", student_names)
        print("Student Ages", student_ages)
    elif selection == 5:
        print("Exiting Program")
        break
    else:
        print("Not Valid Option")
