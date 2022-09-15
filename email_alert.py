import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()
 
# Authentication
pw = input('What is the password of ke.zihlmann@gmail.com?\n')
s.login("ke.zihlmann@gmail.com", pw)
 
# message to be sent
message = "Test"
 
# sending the mail
receiver = input('To whom do you want to send the email? Please enter the email-adress.')
s.sendmail("ke.zihlmann@gmail.com", receiver, message)
 
# terminating the session
s.quit()