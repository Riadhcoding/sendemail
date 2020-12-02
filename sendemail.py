import smtplib
# Comments that you want to send specific information every time
i = ("ENTER YOUR EMAIL : ")
# i = "email@gamil.com"
pw = ("ENTER PASSWORD : ")
# pw = "**********"
s_email = ("SEND TO EMAIL : ")
# s_email = "email@gamil.com"
msg = input ("MESSAGE: ")


server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()

server.login(i,pw)
server.sendmail(i,s_email,msg)

print("massage has been sent")
server.quit()
