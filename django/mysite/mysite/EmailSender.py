__author__ = 'nadav'

import smtplib

class EmailSender:

    fromaddr = '5492nadav@gmail.com'
    username= "5492nadav"
    password= "5341843gabay"


    def __init__(self,userEmailAddress):
        self.userEmailAddress = userEmailAddress


    def login(self,msg):
        # The actual mail send
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(self.username,self.password)
        server.sendmail(self.fromaddr, self.userEmailAddress, msg)
        server.quit()

