from keep_alive import keep_alive

import time

keep_alive()

while True:
  time.sleep(5)
  f = open("time.txt", "a")
  f.write(time.asctime())
  f.write("\n")
  f.close()