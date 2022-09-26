from keep_alive import keep_alive
from get_info import get_info
from send_email import send_email

import time

email_alert = True

keep_alive()

while True:
  t, abfluss, water_level, temperature = get_info()
  
  f = open("abfluss_mellingen.txt", "a")
  f.write(t)
  f.write(", ")
  f.write(abfluss)
  f.write(", ")
  f.write(water_level)
  f.write(", ")
  f.write(temperature)
  f.write("\n")
  f.close()

  if email_alert and int(abfluss)>150:
    send_email(t, abfluss)
    email_alert = False

  time.sleep(600)

