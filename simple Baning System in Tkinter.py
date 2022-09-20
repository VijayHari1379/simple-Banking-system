from tkinter import *
import os

#main screen
master = Tk()
master.title("Banking App")
master.geometry('500x500')
master.configure(background="grey")
#functions
def finish_reg():
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password.get()
    all_accounts = os.listdir()
    

    if name == "" or age == "" or gender ==  "" or password == "" :
        notif.config(fg="red",text="All field requried * ")
        return
    for name_check in all_accounts:
        if name == name_check:
            notif.config(fg="red",text="Accounts already existes")
            return
        else:
            new_file = open(name,"w")
            new_file.write(name+'\n')
            new_file.write(password+'\n')
            new_file.write(age+'\n')
            new_file.write(gender+'\n')
            new_file.write('0')
            new_file.close()
            notif.config(fg="green",text="Account has been created")

def register():

    #var
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global notif
    temp_name=StringVar()
    temp_age=StringVar()
    temp_gender=StringVar()
    temp_password=StringVar()
    
    register_screen = Toplevel(master)
    register_screen.title('Register')
    register_screen.geometry('500x500')
    register_screen.configure(background="grey")
    

    #Label
    l1=Label(register_screen,text="PLEASE ENTER YOUR DETAILS",font=("Lucida Calligraphy",19,"bold"))
    l1.place(x=5,y=15)
    l2=Label(register_screen,text="NAME",font=("Lucida Calligraphy",16,'bold'))
    l2.place(x=30,y=120)
    l3=Label(register_screen,text="AGE",font=("Lucida Calligraphy",16,'bold'))
    l3.place(x=30,y=180)
    l4=Label(register_screen,text="GENDER",font=("Lucida Calligraphy",16,'bold'))
    l4.place(x=30,y=240)
    l5=Label(register_screen,text="PASSWORD",font=("Lucida Calligraphy",16,"bold"))
    l5.place(x=30,y=300)
    notif= Label(register_screen,font=("Lucida Calligraphy",16,"bold"))
    notif.grid(row=6,sticky=N,pady=10)

    #Entrys
    e1=Entry(register_screen,font=("Lucida Calligraphy",16,"bold"),bg='lightpink',textvariable=temp_name,width=15)
    e1.place(x=220,y=120)
    e2=Entry(register_screen,font=("Lucida Calligraphy",16,"bold"),bg='lightpink',textvariable=temp_age,width=15)
    e2.place(x=220,y=180)
    e3=Entry(register_screen,font=("Lucida Calligraphy",16,"bold"),bg='lightpink',textvariable=temp_gender,width=15)
    e3.place(x=220,y=240)
    e4=Entry(register_screen,font=("Lucida Calligraphy",16,"bold"),bg='lightpink',textvariable=temp_password,show="*",width=15)
    e4.place(x=220,y=300)

    #Buttons
    b1=Button(register_screen,text="Register",command=finish_reg,font=("Lucida Calligraphy",16,"bold"),bg='lightblue')
    b1.place(x=70,y=400)
    b2=Button(register_screen,text="Cancel",command=register_screen.destroy,font=("Lucida Calligraphy",16,"bold"),bg='lightblue')
    b2.place(x=300,y=400)
def login_session():
    global login_name
    all_accounts = os.listdir()
    login_name = temp_login_name.get()
    login_password = temp_login_password.get()

    for name in all_accounts:
        if name == login_name:
            file = open(name,"r")
            file_data = file.read()
            file_data = file_data.split('\n')
            password = file_data[1]

            if login_password == password:
                login_screen.destroy()
                account_dashboard = Toplevel(master)
                account_dashboard.title("Dashboard")
                account_dashboard.geometry('500x500')
                #Labels
                l1=Label(account_dashboard ,text="Select Your Option",font=("Lucida Calligraphy",25,"bold"),bg="lightblue")
                l1.place(x=80,y=20)
                l2=Label(account_dashboard ,text="Welcome "+name,font=("Lucida Calligraphy",20,"bold"),fg='red')
                l2.place(x=120,y=90)
                #Button
                b1=Button(account_dashboard,text="Personal Details",font=("Lucida Calligraphy",15,"bold"),bg="lightpink",width=20,command=personal_details)
                b1.place(x=100,y=150)
                b2=Button(account_dashboard,text="Deposit",font=("Lucida Calligraphy",15,"bold"),width=20,command=deposit,bg="lightpink")
                b2.place(x=100,y=250)
                b3=Button(account_dashboard,text="Withdraw",font=("Lucida Calligraphy",15,"bold"),width=20,command=withdraw,bg="lightpink")
                b3.place(x=100,y=350)
                Label(account_dashboard).grid(row=5,sticky=N,pady=10)



                
                return
            else:
                login_notif.config(fg="red",text="Password incorrect!!")
                return
    
    login_notif.config(fg="red",text="No account Found !!!")

def deposit():
    #Vars
    global amount
    global deposit_notif
    global current_balance_label
    amount = StringVar()
    file = open(login_name,"r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[4]
    #Deposit Screen
    deposit_screen = Toplevel(master)
    deposit_screen.title('deposit')
    deposit_screen.geometry('500x500')
    #deposit_screen.configure(background="grey")
    #Label
    l1=Label(deposit_screen , text="Deposit",font=("Lucida Calligraphy",30,"bold"))
    l1.place(x=100,y=60)
    current_balance_label = Label(deposit_screen , text="Current Balance  : "+details_balance,font=("Lucida Calligraphy",18,"bold"))
    current_balance_label.place(x=30,y=150)
    l2=Label(deposit_screen , text="Amount  : ",font=("Lucida Calligraphy",22,"bold"))
    l2.place(x=15,y=240)
    deposit_notif = Label(deposit_screen, font = ("Lucida Calligraphy",20,'bold'))
    deposit_notif.grid(row=4,sticky=N,pady=10)
    #Entry
    e1=Entry(deposit_screen,textvariable=amount,font = ("Lucida Calligraphy",20,'bold'),width=15,bg="lightpink")
    e1.place(x=200,y=240)
    #Button
    b1=Button(deposit_screen,text="Sumbit",font=("Lucida Calligraphy",17,"bold"),command=finish_deposit,bg="lightblue")
    b1.place(x=70,y=400)
    b2=Button(deposit_screen,text="Cancel",font=("Lucida Calligraphy",17,"bold"),command=deposit_screen.destroy,bg="lightblue")
    b2.place(x=300,y=400)

def finish_deposit():
    if amount.get() ==  "":
        deposit_notif.config(text="Amount is required!!",fg='red')
        return
    if float(amount.get()) <=0:
        deposit_notif.config(text="Negative currency is not accepted",fg='red')
        return
    file = open(login_name,"r+")
    file_data = file.read()
    details = file_data.split("\n")
    current_balance = details[4]
    update_balance = current_balance
    update_balance = float(update_balance)+float(amount.get())
    file_data  = file_data.replace(current_balance,str(update_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    current_balance_label.config(text="Current Balance  : "+str(update_balance),fg="green")
    deposit_notif.config(text="Balance Update",fg="green")
    
        
    

def withdraw():
    #Vars
    global withdraw_amount
    global withdraw_notif
    global current_balance_label
    withdraw_amount = StringVar()
    file = open(login_name,"r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[4]
    #Deposit Screen
    withdraw_screen = Toplevel(master)
    withdraw_screen.title('withdraw')
    withdraw_screen.geometry('500x500')
    
    #Label
    l1=Label(withdraw_screen , text="WITHDRAW",font=("Lucida Calligraphy",30,"bold"),fg='black')
    l1.place(x=100,y=60)
    current_balance_label = Label(withdraw_screen , text="Current Balance  : "+details_balance,font=("Lucida Calligraphy",18,"bold"))
    current_balance_label.place(x=30,y=150)
    l2=Label(withdraw_screen , text="Amount  : ",font=("Lucida Calligraphy",20,"bold"))
    l2.place(x=15,y=280)
    withdraw_notif = Label(withdraw_screen, font = ("Lucida Calligraphy",20,'bold'))
    withdraw_notif.grid(row=4,sticky=N,pady=10)
    #Entry
    e1=Entry(withdraw_screen,textvariable=withdraw_amount,font=("Lucida Calligraphy",20,"bold"),width=15,bg="lightpink")
    e1.place(x=200,y=280)
    #Button
    b1=Button(withdraw_screen,text="Submit",font=("Lucida Calligraphy",17,"bold"),command=finish_withdraw,bg='lightblue')
    b1.place(x=70,y=400)
    b2=Button(withdraw_screen,text="Cancel",font=("Lucida Calligraphy",17,"bold"),command=withdraw_screen.destroy,bg='lightblue')
    b2.place(x=300,y=400)

def finish_withdraw():
    if withdraw_amount.get() ==  "":
        withdraw_notif.config(text="Amount is required!!",fg='red')
        return
    if float(withdraw_amount.get()) <=0:
        withdraw_notif.config(text="Negative currency is not accepted",fg='red')
        return
    file = open(login_name,"r+")
    file_data = file.read()
    details = file_data.split("\n")
    current_balance = details[4]
    


    if float(withdraw_amount.get()) >float(current_balance):
        withdraw_notif.config(text='Insufficiet Funds!!!',fg='red')
        return
    
    update_balance = current_balance
    update_balance = float(update_balance) - float(withdraw_amount.get())
    file_data  = file_data.replace(current_balance,str(update_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    current_balance_label.config(text="Current Balance  : "+str(update_balance),fg="green")
    withdraw_notif.config(text="Balance Update",fg="green")
    


def personal_details():
    #vars
    file = open(login_name,"r")
    file_data = file.read()
    user_details = file_data.split("\n")
    details_name = user_details[0]
    details_age = user_details[2]
    details_gender = user_details[3]
    details_balance = user_details[4]
    #personal details screen
    personal_details_screen=Toplevel(master)
    personal_details_screen.title("Personal Details")
    personal_details_screen.geometry('500x500')
    
    #Labels
    l1=Label(personal_details_screen,text="Personal Details",font=("Lucida Calligraphy",25,"bold"),bg='blue')
    l1.place(x=60,y=20)
    l2=Label(personal_details_screen,text="Name  : " + details_name,font=("Lucida Calligraphy",19,"bold"))
    l2.place(x=90,y=100)
    l3=Label(personal_details_screen,text="Age  : " + details_age,font=("Lucida Calligraphy",19,"bold"))
    l3.place(x=90,y=200)
    l4=Label(personal_details_screen,text="Gender  : " + details_gender,font=("Lucida Calligraphy",19,"bold"))
    l4.place(x=90,y=300)
    l5=Label(personal_details_screen,text="Balance  : " + details_balance,font=("Lucida Calligraphy",19,"bold"))
    l5.place(x=90,y=400)
    
    
    



    


def login():
    #var
    global temp_login_name
    global temp_login_password
    global login_notif
    global login_screen
    temp_login_name=StringVar()
    temp_login_password=StringVar()
    
    #Login Screen
    login_screen = Toplevel(master)
    login_screen.title('Login')
    login_screen.geometry('500x500')
    login_screen.configure(background="grey")
    #Labels
    l1=Label(login_screen,text="Login Your Account",font=("Lucida Calligraphy",25,"bold"))
    l1.place(x=60,y=15)
    l2=Label(login_screen,text="USERNAME",font=("Lucida Calligraphy",12,"bold"))
    l2.place(x=30,y=150)
    l3=Label(login_screen,text="PASSWORD",font=("Lucida Calligraphy",12,"bold"))
    l3.place(x=30,y=250)
    login_notif = Label(login_screen,font=("Lucida Calligraphy",12,"bold"))
    login_notif.grid(row=4,sticky=N)

    #Entry
    e1=Entry(login_screen,font=("Lucida Calligraphy",16,"bold") ,width=15, textvariable=temp_login_name,bg='lightpink')
    e1.place(x=210,y=150)
    e2=Entry(login_screen ,font=("Lucida Calligraphy",16,"bold"),width=15, textvariable=temp_login_password,show="*",bg='lightpink')
    e2.place(x=210,y=250)

    #Buttons
    b1=Button(login_screen,text="Login",command=login_session,width=10,font=("Lucida Calligraphy",12,"bold"),bg='lightblue')
    b1.place(x=70,y=400)
    b2=Button(login_screen,text="Cancel",command=login_screen.destroy,width=10,font=("Lucida Calligraphy",12,"bold"),bg='lightblue')
    b2.place(x=300,y=400)


#labels
l=Label(master, text="ICICI BANK",font=("Lucida Calligraphy",30,"bold"))
l.place(x=100,y=50)

#Label(master, text="The most secure bank you probably used",font=("Lucida Calligraphy",14)).grid(row=1,sticky=N)


#buttons
b1=Button(master,text="Register",font=("Lucida Calligraphy",14,"bold"),width=15,command=register,bg='pink')
b1.place(x=130,y=150)
b2=Button(master,text="Login",font=("Lucida Calligraphy",14,"bold"),width=15,command=login,bg='pink')
b2.place(x=130,y=250)


master.mainloop()
