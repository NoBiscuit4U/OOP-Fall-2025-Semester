while True:
    info_dict={}
    student_info=[]
    student_id=[]
    options=["Add Student Information","Remove Student Information","Replace Student Information","Print All Student Information","Quit"]

    for i in range(0,len(options)):
        print(i," "+options[i])

    user_select=int(input("Enter Desired Option: "))

    if user_select <= 2:
        if user_select != 1:
            student_info = input("Enter Student Information in Format: StudentID, Name, Major, Year, Credits, GPA: ").split(",")

    if user_select == 0 :
        info_dict.update({
            student_info[0]: {
                "Name": student_info[1],
                "Major": student_info[2],
                "Year": student_info[3],
                "Credits": student_info[4],
                "GPA": student_info[5],
            }
        })
    if user_select == 1:
        if student_id in info_dict.keys():
            del info_dict[student_id]
        else:
            print("Student ID not Found")
    if user_select == 2:
        i=0
        if student_id in info_dict.keys():
            for key in info_dict[student_id].keys():
                info_dict[key]=student_info[i]
                i+=1
        else:
            print("Student ID not Found")
    if user_select == 3:
        for record in info_dict.items():
            print(record)
    if user_select == 4:
        break