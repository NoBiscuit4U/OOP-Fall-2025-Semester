table_num=int(input("Enter Desired Number to get Multiplication Table Of: "))
table_size=(int(input("Enter Desired Size: "))+1)

print("Multiplication Table of: ",table_num)
for i in range(1,table_size):
    print(i,"*",table_num," = ",table_num*i)


