desired_inputs=[]
projects={}
options=["Project Initiation","Project Closure","Project Progress Update",
         "Print Specific Project","Print All","Close Application"]
temp_proj_dict={
    "Project_Title":"",
    "Managers":[],
    "Start_Date":"",
    "End_Date":"",
    "Sponsor":"",
    "Budget":"",
    "Technologies":[],
    "Team_Members":[]
}

while True:
    print("-----")
    for i in range(0,len(options)):
        print(i," "+options[i])

    selected=int(input("Select Desired Option Number: "))

    if selected == 0:
        proj_num=len(temp_proj_dict)
        new_proj_num="proj"+str(proj_num)
        new_proj_values=temp_proj_dict
        for key in temp_proj_dict.keys():
            print("-----")
            print("Add comma between values when adding more than 1")
            user_input=input("Enter Value/Values for "+key+": ")

            if user_input.find(",")!=-1:
                user_input=user_input.split(",")

            new_proj_values[key]=user_input

        projects.update({proj_num:new_proj_values})

    elif selected == 1:
        proj_title=input("Enter Project Title for Removal: ")
        key_for_removal=""
        for key in projects.keys():
            if proj_title == projects[key]["Project_Title"]:
                key_for_removal=key

        del projects[key_for_removal]

    elif selected == 2:
        target_proj = input("Enter Title of Project For Editing: ")

        print("-----")
        for key in temp_proj_dict.keys():
            print(key)
        print("-----")

        chosen_value=input("Enter Value To Change: ")

        if chosen_value not in projects.keys():
            print("Invalid Value")
            break
        else:
            print("Add comma between values when adding more than 1")
            new_value=input("Enter New Value/Values: ")

            if new_value.find(",") != -1:
                new_value = new_value.split(",")

            for key in temp_proj_dict.keys():
                if projects[key]["Project_Title"] == target_proj:
                    projects[key][chosen_value] = new_value

    #elif selected ==3:
    ##FIX

    elif selected == 4:
        for proj in projects.items():
            print("-----")
            print("Project Values: ",proj)





