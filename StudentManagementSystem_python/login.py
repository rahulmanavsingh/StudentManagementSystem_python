from tkinter import *
from tkinter import messagebox
import mysql.connector


background="#06283D"
framebg="#EDEDED"
framebg="#06283D"

global trail_no
trail_no=0

def trail():
    global trail_no
    trail_no+=1
    print("Trail no is ",trail_no)
    if trail_no==3:
        messagebox.showwarning("Warning","You have tried more then limit!!")
        root.destroy()      #program close




def loginuser():
    username = user.get()
    password = code.get()

    if username == "" or username == "UserID" or password == "" or password == "Password":
        messagebox.showerror("Entry error", "Type username or password!!")
    else:
        try:
            mydb = mysql.connector.connect(host='localhost', user='root', password="123", database="studentregistration")
            mycursor = mydb.cursor()
            print("Connected to the database!!!")
        except:
            messagebox.showerror("Connection", "Failed to establish database connection!!!!")
            return
    
        command = "USE studentregistration"
        mycursor.execute(command)

        command = "SELECT * FROM login WHERE Username = %s AND Password = %s"
        mycursor.execute(command, (username, password))
        myresult = mycursor.fetchone()
        print(myresult)

        if myresult is None:
            messagebox.showinfo("Invalid", "Invalid username and password!!!!")

            # Since users can attempt multiple times and crack the password, let's limit the number of attempts to 3
            trail()
        else:
            messagebox.showinfo("Login", "Successful Login!!!")
            root.destroy()
            import main

def register():
    root.destroy()
    import register


root=Tk()
root.title("Login System")
root.geometry("1250x700+210+100")
root.config(bg=background)
root.resizable(False,False)



#icon image
image_icon=PhotoImage(file="Images/icon.png")
root.iconphoto(False,image_icon)


#background image
frame=Frame(root,bg="red")
frame.pack(fill=Y)

backgroundimage=PhotoImage(file="Images/LOGIN.png")
Label(frame,image=backgroundimage).pack()

##############USER ENTRY
def user_enter(e):
    user.delete(0,'end')

def user_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'UserID')



user= Entry(frame,width=18,fg="#fff",border=0,bg="#375174",font=('Arial Bold',24))
user.insert(0,'UserID')
user.bind("<FocusIn>", user_enter)
user.bind("<FocusOut>", user_leave)
user.place(x=500,y=315)


##############PasswordENTRY
def password_enter(e):
    code.delete(0,'end')

def password_leave(e):
    if code.get()=='':
        code.insert(0,'Password')



code= Entry(frame,width=18,fg="#fff",border=0,bg="#375174",font=('Arial Bold',24))
code.insert(0,'Password')
code.bind("<FocusIn>", password_enter)
code.bind("<FocusOut>", password_leave)
code.place(x=500,y=410 )

###########HIDE AND SHOW BUTTON
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
eyeButton=Button(frame,image=openeye,bg="#375174",bd=0,command=hide)
eyeButton.place(x=780,y=410)

####################################################

loginButton=Button(root,text="LOGIN",bg="#1f5675",width=10,height=1,font=("arial",16,'bold'),bd=0,command=loginuser)
loginButton.place(x=570,y=600)

label=Label(root,text="Don't have an account?",fg="#fff",bg="#00264d",font=('Microsoft YaHei UI Light',9))
label.place(x=500,y=500)

registerButton=Button(root,width=10,text="add new user",border=0,bg="#00264d",cursor='hand2',fg="#57a1f8",command=register)
registerButton.place(x=650,y=500)



root.mainloop()
