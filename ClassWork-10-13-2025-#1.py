import pickle

with open("cred_info","rb") as f:
    load_dict = pickle.load(f)

username=input("Enter Username: ")
password=input("Enter Password: ")

for user in load_dict.keys():
    cred_name=load_dict[user]["username"]
    cred_password=load_dict[user]["password"]
    if cred_name == username and cred_password == password:
        print("Credential Verified")
        break

f.close()
