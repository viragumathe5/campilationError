import sys
from tkinter import *
import smtplib


#GUI formalities
tab = Tk()
tab.title("Instant MAILBOx")
tab.geometry('800x500+120+120')


#declearing textvariables
usr_log  = StringVar()
usr_pass = StringVar()
rec_log  = StringVar()
mail_sub = StringVar() 
mail_cnt = StringVar()


#function collection and sending

def coll_send():
    
    #sr2_log  = StringVar()
    #sr2_pass = StringVar()
    #c2_log  = StringVar()
    #ail2_sub = StringVar() 
    #ail2_cnt = StringVar()

    usr2_log  = usr_log.get()
    usr2_pass = usr_pass.get()
    rec2_log  = rec_log.get()
    mail2_sub = mail_sub.get() 
    mail2_cnt = mail_cnt.get()

    

    go = smtplib.SMTP('smtp.gmail.com', 587)

    go.ehlo()

    go.starttls()

    go.login(usr2_log, usr2_pass)
    
   
    #exception handling for errors

    try:
        go.sendmail(usr2_log, rec2_log, 'subject: %r \n\n %r' %(mail2_sub, mail2_cnt) )

    
    
    except:
        tab2 = Tk()     
        tab2.title('error found') 
        tab2.geometry('300x300')

        Label(tab2, text = "Invalid inputs").pack()
        
        
    
    
    go.close




#intro for gmail users

_intro = Label(tab, text = "\n\nHello! I made this mailbox only for gmail users and make shure you have enabled the option for less secured apps \nor do it from url:https://myaccount.google.com/lesssecureapps").pack()



#taking login id from user

_loginid = Label(tab, text = "\n\nPlease enter your email adress").pack()
_ent_usr_log = Entry(tab, textvariable = usr_log, width = 40).pack()


#taking password from user

_password = Label(tab, text = "Please enter your password").pack()
_ent_usr_pass = Entry(tab, textvariable = usr_pass, width = 40).pack()


#taking receivers id from user

_receiverid = Label(tab, text = "Please enter the receivers emailid").pack()
_ent_rec_log = Entry(tab, textvariable = rec_log, width = 40).pack()


#taking subject from user for mail

_subject = Label(tab, text = "Please enter the subject for the email").pack()
_ent_mail_sub = Entry(tab, textvariable = mail_sub, width = 40).pack()



#taking content from user for mail

_content = Label(tab, text = "Please enter the content for the email").pack()    
_ent_mail_cnt = Entry(tab, textvariable = mail_cnt, width = 40).pack()


#button for sending mail 

button_1 = Button(tab, text = "SEND MAIL", fg = "black", command = coll_send).pack()




#end of the GUI
tab.mainloop()
