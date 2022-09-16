from keep_alive import keep_alive

import time

keep_alive()

while True:
  time.sleep(15)
  f = open("time.txt", "a")
  f.write(time.asctime())
  f.write("\n")
  f.close()
  f2 = open("abfluss_mellingen.txt", "a")
  f2.write(time.asctime())
  f2.write(" ")
  f2.write(str(get_info()))
  f2.close()