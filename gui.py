from tkinter import *
from tkinter import messagebox

from PIL import ImageTk,Image

root=Tk()

def login_handel():
    email=email_input.get()
    Password=Password_input.get()
    if email=='Prashant@gmail.com' and Password=='805234':
        messagebox.showinfo('Success','Login successfully')
    else:
        messagebox.showerror('Error','Login failed')
        
        

root.title('Login form')

root.iconbitmap('favicon.ico')

root.configure(background='#0096DC')

img=Image.open('image.png')

resized_img=img.resize((100,100))

img=ImageTk.PhotoImage(resized_img)

img_label=Label(root,image=img)

img_label.pack(pady=(30,20))

text_label=Label(root,text='PrasG',fg='white',bg='#0096DC')

text_label.pack(pady=(2,5))

text_label.config(font=('verdana', 24))

email_label=Label(root,text='Enter Email', fg='white', bg='#0096DC')

email_label.pack()

email_label.config(font=('verdana',12))

email_input=Entry(root, width='40')

email_input.pack(ipady=4,pady=(1,10))

Password_label=Label(root,text='Enter Password', fg='white', bg='#0096DC')

Password_label.pack()

Password_label.config(font=('verdana',12))

Password_input=Entry(root, width='40')

Password_input.pack(ipady=4,pady=(1,10))

login_btn=Button(root,text='Login here', bg='white', fg='black' ,width=20, height=1,command=login_handel)
login_btn.pack(pady=(10,20))
login_btn.config(font=('verdana',10))


root.geometry('300x450')
 


root.mainloop()