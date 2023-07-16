from tkinter import *
from tkinter  import messagebox
import mysql.connector

background="#06283D"
framebg="#EDEDED"
framefg="#06283D"

root=Tk()
root.title("Student Registration System")
root.geometry("1250x700+210+100")
root.config(bg=background)
root.resizable(False,False)


def register():
    username=user.get()
    password=code.get()
    admincode=adminaccess.get()

    # print(username,passowrd,admincode)

    if admincode=="9955":

        if(username=="" or username=="UserID") or (password=="Password" or password==""):
            messagebox.showerror("Entry error!!","Type username or passoword!!!")
        else:
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',password='123')
                mycursor=mydb.cursor()
                print("Connect Stablished!!!!!!")

            except:
                messagebox.showerror("Connection","Database connection not stablished  !!")

            try:
                command="create database studentregistration"
                mycursor.execute(command)
                
                command="use studentregistration"
                mycursor.execute(command)

                command="create table login (user int auto_increment key not null, Username varchar(50),Password varchar(100))"
                mycursor.execute(command)

            except:
                # mycursor.execute("use studentregistration")
                # mydb=mysql.connector.connect(host='localhost',user='root',password='123',database="studentregistration")
                # mycursor=mydb.cursor()

                # command="insert into login(Username,Password) values(%s,%s)"
                # mydb.commit()
                # mydb.close()
                # messagebox.showinfo("Register","New User added Sucessfully!!!")
                mycursor.execute("use studentregistration")
                mydb = mysql.connector.connect(host='localhost', user='root', password='123', database="studentregistration")
                mycursor = mydb.cursor()

                command = "insert into login(Username, Password) values(%s, %s)"
                mycursor.execute(command, (username, password))  # Replace username_value and password_value with actual values
                mydb.commit()

                mydb.close()
                messagebox.showinfo("Register", "New User added successfully!!!")
    


    else:
        messagebox.showerror("Admin code!","Input Correct Admin code to add new user!!!")



















def login():
    root.destroy() #close current window
    import login

#icon image
image_icon=PhotoImage(file="Images/icon.png")
root.iconphoto(False,image_icon)

#background image
frame=Frame(root,bg="red")
frame.pack(fill=Y)

backgroundimage=PhotoImage(file="Images/register.png")
Label(frame,image=backgroundimage).pack()


adminaccess=Entry(frame,width=15,fg="#000",border=0,bg="#e8ecf7",font=("Arial Bold",20),show="*")
adminaccess.focus()
adminaccess.place(x=550,y=280)

##############################-----User Entry
def user_enter(e):
    user.delete(0,'end')

def user_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'UserID')

user = Entry(frame, width=18, fg="#fff", bg="#375174", border=0, font=("Arial Bold",20))
user.insert(0, "UserID")
user.bind("<FocusIn>", user_enter)
user.bind("<FocusOut>", user_leave)
user.place(x=500, y=380)


##############################-----Password Entry
def password_enter(e):
    code.delete(0,'end')

def password_leave(e):
    if code.get()=='':
        code.insert(0, 'Password')

code = Entry(frame, width=18, fg="#fff", bg="#375174", border=0, font=("Arial Bold",20))
code.insert(0, "Password")
code.bind("<FocusIn>", password_enter)
code.bind("<FocusOut>", password_leave)
code.place(x=500, y=470)
#copy from here
##################################################################

button_mode=True

def hide():
    global button_mode
    if button_mode:
        eyeButton.config(image=closeeye,activebackground="white")
        code.config(show="*")
        button_mode=False
    else:
        eyeButton.config(image=openeye,activebackground="white")
        code.config(show="")
        button_mode=True

openeye=PhotoImage(file="Images/openeye.png")
closeeye=PhotoImage(file="Images/close eye.png")

eyeButton=Button(root,image=openeye,bg="#375174",bd=0,command=hide)
eyeButton.place(x=780,y=470)


####################################################################

regis_button=Button(root,text="ADD NEW USER",bg="#455c88",fg="white",width=13,height=1,font=("Arial",16,"bold"),
bd=0,command=register)
regis_button.place(x=530,y=600)


backbuttonimage=PhotoImage(file="Images/backbutton.png")
Backbutton=Button(root,image=backbuttonimage,fg="#deeefb",command=login)
Backbutton.place(x=20,y=15)



root.mainloop()