import smtplib

def send_email(t, abfluss):
  with open('email_infos.txt') as f:
    sender_email = f.readline()
    sender_pw = f.readline()
    receiver_email = f.readline()

  f.close()

  # creates SMTP session
  s = smtplib.SMTP('smtp.gmail.com', 587)

  # start TLS for security
  s.starttls()
 
  # Authentication
  s.login(sender_email, sender_pw)
 
  # message to be sent
  message = """\
Subject: Mellingen Alarm

Um """ + t + """ betrug die Abflussmenge in Mellingen """ + abfluss + """ m^3/s. \nSurf's up!!!"""
 
  # sending the mail
  s.sendmail(sender_email, receiver_email, message)
 
  # terminating the session
  s.quit()
