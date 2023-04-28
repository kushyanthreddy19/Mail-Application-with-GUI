from tkinter import *
#import smtplib
#from email.message import EmailMessage
#import ssl
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email , To , Content




#main screen

master = Tk()
master.title('Email App')


# function
def send():
    
        #sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('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'))
        sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('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'))
        username = temp_username.get()
        password = temp_password.get()
        to = To(temp_receiver.get())
        subject = temp_subject.get()
        body = temp_body.get()

        if username == '' or  password == "" or to == '' or subject =='' or body == '':
            notif.config(text="All fields are required",fg = 'red')
            return
        else:
            mail = Mail(username,to,subject,body)
            mail_json = mail.get()
            response = sg.client.mail.send.post(request_body = mail_json)
            print(response.status_code)
            print(response.headers)

            # finalMessage = 'Subject: {}\n\n{}'.format(subject,body)
            # server = smtplib.SMTP('smtp.gmail.com',465)
            # server.starttls()
            # server.login(username,password)
            # notif.config(text="login successful" , fg = 'green')
            # server.sendmail(username,to,finalMessage)
            # notif.config(text=" Email has been sent successfully" , fg = 'green')
            # em = EmailMessage()
            # em['From'] = username
            # em['To'] = to
            # em['subject'] = subject
            # em.set_content(body)
            
            # context = ssl.create_default_context()

            # with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
            #     smtp.login(username,password)
            #     smtp.sendmail(username , to , em.as_string)
    
            notif.config(text = "error  sending email",fg = 'red') 
        
def reset():
    usernameEntry.delete(0,'end')
    passwordEntry.delete(0,'end')
    receiverEntry.delete(0,'end')
    subjectEntry.delete(0,'end')
    subjectbody.delete(0,'end')

#graphics

Label(master,text = 'Custom Email App',font=('calibri',45)).grid(row = 0, sticky = N)
Label(master,text = 'Use This app to send Email',font=('calibri',18)).grid(row = 6,sticky = W, padx = 7)

Label(master,text = 'Email',font=('calibri',14)).grid(row = 10,sticky = W, padx = 10, pady = 12)
Label(master,text = 'Password',font=('calibri',13)).grid(row = 12,sticky = W, pady = 5)
Label(master,text = 'To',font=('calibri',14)).grid(row = 14,sticky = W, padx = 5, pady = 5)
Label(master,text = 'Subject',font=('calibri',14)).grid(row = 16,sticky = W, padx = 5, pady = 5)
Label(master,text = 'Body',font=('calibri',14)).grid(row = 18,sticky = W, padx = 5, pady = 5)

notif = Label(master,text = '',font=('calibri',14))
notif.grid(row = 25,sticky = W, padx = 5, pady = 5)

#storage

temp_username = StringVar()
temp_password = StringVar()
temp_receiver = StringVar()
temp_subject = StringVar()
temp_body = StringVar()

# Entries

usernameEntry = Entry(master,textvariable = temp_username)
usernameEntry.grid(row =10,column = 0)
passwordEntry = Entry(master,show = "*", textvariable = temp_password)
passwordEntry.grid(row = 12,column = 0)
receiverEntry = Entry(master,textvariable = temp_receiver)
receiverEntry.grid(row = 14,column = 0)
subjectEntry = Entry(master,textvariable = temp_subject)
subjectEntry.grid(row = 16,column = 0)
subjectbody = Entry(master,textvariable = temp_body)
subjectbody.grid(row = 18,column = 0)

# Buttons

Button(master,text = "send",command=send).grid(row=22,padx = 5,pady = 8,sticky = W)
Button(master,text = "Reset",command=reset).grid(row=22,padx = 45,pady = 8,sticky = W)

 
    
master.mainloop() 