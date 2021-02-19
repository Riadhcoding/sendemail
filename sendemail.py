import smtplib
# Comments that you want to send specific information every time
i = ("ENTER YOUR EMAIL (hotmail) : ")
# i = "email@hotmail.com" or "email@live.com"
pw = ("ENTER PASSWORD : ")
# pw = "**********"
s_email = ("SEND TO EMAIL : ")
# s_email = "email@hotmail.com" or "email@live.com"
msg = input ("MESSAGE: ")

server = smtplib.SMTP('smtp-mail.outlook.com:587') # defining outlook server:smtp-mail.outlook.com + ":" + port
server.ehlo()
server.starttls()

server.login(i,pw)
server.sendmail(i,s_email,msg)

print("massage has been sent")
server.quit()
