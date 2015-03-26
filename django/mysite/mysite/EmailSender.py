__author__ = 'nadav'

import smtplib

class EmailSender:

    fromaddr = 'yourfacebookjobsearch@gmail.com'
    username= "yourfacebookjobsearch"
    password= "duda1234"


    def __init__(self,userEmailAddress):
        self.userEmailAddress = userEmailAddress


    def login(self,msg):
        # The actual mail send
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(self.username,self.password)
        server.sendmail(self.fromaddr, self.userEmailAddress, msg)
        server.quit()

