from tkinter import *
import os

def restart():
    os.system('shutdown/r /t 1')
def restart_time():
     os.system('shutdown /r /t 12')
def log_out():
     os.system('shutdown  -1')
def shutdown():
      os.system('shutdown  /s /t 20')
     



root=Tk()
root.title('shutdown app')
root.geometry('500x400')
root.config(bg='yellow')

button_res=Button(root,text='Restart',font=('Time New Roman',20,'bold'),bg='pink',relief=RAISED,cursor='plus',command=restart)
button_res.place(x=190,y=30,height=40,width=100)

button_tm=Button(root,text='Restart time',font=('Time New Roman',20,'bold'),bg='pink',relief=RAISED,cursor='plus',command=restart_time)
button_tm.place(x=160,y=100,height=40,width=160)

button_lg=Button(root,text='logout ',font=('Time New Roman',20,'bold'),bg='pink',relief=RAISED,cursor='plus',command=log_out)
button_lg.place(x=160,y=170,height=40,width=160)

button_s=Button(root,text='Shutdown',font=('Time New Roman',20,'bold'),bg='pink',relief=RAISED,cursor='plus',command=shutdown)
button_s.place(x=135,y=240,height=40,width=200)


root.mainloop()
