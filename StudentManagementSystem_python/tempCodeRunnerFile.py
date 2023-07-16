def password_enter(e):
    code.delete(0,'end')

def password_leave(e):
    if code.get()=='':
        code.insert(0,'Password')