import tkinter
from tkinter import messagebox
import re

#=====LOGIN======
sign_in=[]

def login():
    user_name=input("Enter User Name: ")
    password=input("Enter Password: ")
    sign_in.append((user_name,password))
    print("✅ Sign In Successful!")
us_name=('ali110')
ps_word=('1234')
def logout():
    sign_in.clear()
    print("✅ Logged Out Successfully!")

def verify_login():
    if login==us_name: 
        messagebox("✅ Username Correct")
    elif login==ps_word:
        messagebox(" Password Correct") 
    else:
        messagebox("Invalid username or password")



#-------login frame--------
root = tkinter.Tk()
root.title("Login")
root.geometry("300x200")
root.config(bg="#e0f7fa")
# Username Label and Entry
username_label = tkinter.Label(root, text="Username:", bg="#e0f7fa")
username_label.pack(pady=10)
username_entry = tkinter.Entry(root)
username_entry.pack(pady=5) 
# Password Label and Entry
password_label = tkinter.Label(root, text="Password:", bg="#e0f7fa")
password_label.pack(pady=10)
password_entry = tkinter.Entry(root, show="*")
password_entry.pack(pady=5)
#----- verify login button-----
tkinter.Button(root, text="Login", bg="#00796b", fg="white", command=verify_login).pack(pady=15)



root.mainloop()