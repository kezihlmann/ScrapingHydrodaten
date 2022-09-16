import smtplib

with open('email_infos.txt') as f:
    sender_email = f.readline()
    sender_pw = f.readline()
    receiver_email = f.readline()

f.close()

print(sender_email)
print(sender_pw)
print(receiver_email)

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()
 
# Authentication
s.login(sender_email, sender_pw)
 
# message to be sent
message = "Test"
 
# sending the mail
s.sendmail(sender_email, receiver_email, message)
 
# terminating the session
s.quit()