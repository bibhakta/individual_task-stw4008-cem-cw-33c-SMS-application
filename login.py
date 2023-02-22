from tkinter import *            #tkinter module import garya
from tkinter import messagebox
import sqlite3


root = Tk()                     
root.title("Login Page")              
root.iconbitmap('img/students.ico')    
root.geometry('900x500+200+2')
root.configure(bg='#fff')  #bg color change 


        
# login page start from here

def forget_pass():
    def change_pass():
        try:
            if gmail_f.get()=="" or pas_1.get()=="" or pas_2.get()=="":
                messagebox.showerror("error","some field are empty")
            elif pas_1.get()!=pas_2.get():
                messagebox.showerror("error","Password didnot matches")
            else:
                db=sqlite3.connect("registers_std.db")
                cursor=db.cursor()
                query='select * from Account where Email=?'
                cursor.execute(query,[(gmail_f.get())])
                row=cursor.fetchone()
                if row==None:
                    messagebox.showerror("Error","Email doesnot exist")
                else:
                    query='''UPDATE Account SET Password=?, ConfirmPass=? where Email=?'''
                    cursor.execute(query,[pas_1.get(),  pas_2.get(),gmail_f.get(),])
                    db.commit()
                    db.close()
                    messagebox.showinfo("Success","Password change successfully")
                    forget.destroy()
        except:
            messagebox.showerror("database","Connectivity error")


            
    forget = Toplevel()                      
    forget.title("Recover password")              
    forget.iconbitmap('img/students.ico')     
    forget.geometry('500x500+100+2')
   
    forget.configure(bg='#fff')  #bg color change garne
    # image3=PhotoImage(file='img/loggg.png') #adding img
    # Label(forget,image=image3,bg='white',width=800,height=800).place(x=290,y=30) #placing img
    # Label.image= image3 #Image was not showing so internal image varialble to object
    header=Label(forget,text='RESET YOUR PASSWORD',fg='#3751FE', bg='white',font=('Gill Sans MT',23,'bold'))
    header.place(x=50,y=10)
    pleas=Label(forget,text='Please input your information on fields.',fg='black', bg='white',font=('roboto',8))
    pleas.place(x=50,y=50)
    gm=Label(forget,text='Email',fg='black', bg='white',font=('roboto',10))
    gm.place(x=50,y=100)
    gmail_f=Entry(forget,width=25,fg='#404040',border=0,highlightthickness=1,highlightbackground='#F1F0FD',font=('roboto',9))
    gmail_f.place(x=50,y=125,height=25)
    pas=Label(forget,text='Confirm Password',fg='black', bg='white',font=('roboto',10))
    pas.place(x=50,y=230)
    pas_1=Entry(forget,width=25,fg='#404040',border=0,highlightthickness=1,highlightbackground='#F1F0FD',font=('roboto',9))
    pas_1.place(x=50,y=260,height=25)
    pas2=Label(forget,text='Create New Password',fg='black', bg='white',font=('roboto',10))
    pas2.place(x=50,y=160)
    pas_2=Entry(forget,width=25,fg='#404040',border=0,highlightthickness=1,highlightbackground='#F1F0FD',font=('roboto',9))
    pas_2.place(x=50,y=190,height=25)
    sub=Button(forget,width=10,pady=7,text='Submit',bg='#3751FE',fg='white',border=0,command=change_pass)
    sub.place(x=50,y=300)
    go=Label(forget,text='Go back to Login?',fg='black', bg='white',font=('roboto',8))
    go.place(x=100,y=400)
    log=Button(forget,width=6,pady=7,text='Login',bg='white',fg='#3751FE',font=('roboto',8),border=0)
    log.place(x=195,y=395)

def login():
    def opensignup():
        root.destroy()
        import registration
    def openapp():
        root.destroy()
        import newsys
    def login_account():
        try:
            connection=sqlite3.connect("registers_std.db")
            mycur=connection.cursor()
            for row in mycur.execute("Select * from Account"):
                email_log=row[3]
                pas_log=row[4]
        except Exception as ep:
            messagebox.showerror('error','Database connectivity Issue,Please try again')
            
        email5=email1.get()
        pas5=pas1.get()
        if email1.get()=='' or pas1.get()=='':
            messagebox.showerror('error','one or more fields empty!')
        elif "@" and ".com" not in email5:
            messagebox.showerror("error","Invalid Email")
        elif len(pas5)<5:
            messagebox.showerror("error","password must be more than 5 letter")
        elif email5==email_log and pas5==pas_log:
            messagebox.showinfo('Login status','Logged in successful')
            import Admin_Dashboard
        else:
            messagebox.showerror('Error','username or password is invalid')


    global email1,pas1
    image1=PhotoImage(file='img/loggg.png') #adding img
    Label(root,image=image1,bg='white').place(x=320,y=40) #placing img
    Label.image= image1 #Image was not showing so internal image varialble to object
    header=Label(root,text='LOG IN',fg='#3751FE', bg='white',font=('Gill Sans MT',30,'bold'))
    header.place(x=50,y=50)
    para=Label(root,text='Please input your information on fields.',fg='black', bg='white',font=('roboto',8))
    para.place(x=50,y=100)
    para4=Label(root,text='Enter Your Email',fg='black', bg='white',font=('roboto',8))
    para4.place(x=50,y=190)
    email1=Entry(root,width=30,fg='black',border=0,highlightthickness=1,highlightbackground='#F1F0FD',font=('roboto',9))
    email1.place(x=50,y=210,height=40)
    para5=Label(root,text='Enter Your Password',fg='black', bg='white',font=('roboto',8))
    para5.place(x=50,y=270)
    pas1=Entry(root,width=30,fg='black',border=0,highlightthickness=1,highlightbackground='#F1F0FD',font=('roboto',9))
    pas1.place(x=50,y=290,height=40)
    Button(root,width=18,pady=7,text='Forgot your password?',bg='white',fg='#3751FE',font=('roboto',8),border=0,command=forget_pass).place(x=50,y=340)
    Button(root,width=10,pady=7,text='Log in',bg='#3751FE',fg='white',border=0,command=login_account).place(x=50,y=380)
    para3=Label(root,text='Dont have account yet?',fg='black', bg='white',font=('roboto',8))
    para3.place(x=100,y=450)
    Button(root,width=6,pady=7,text='Sign in',bg='white',fg='#3751FE',font=('roboto',8),border=0,command=opensignup).place(x=220,y=444)  
login()

root.mainloop()