from keep_alive import keep_alive
from get_info import get_info

import time

keep_alive()

while True:
  time.sleep(15)
  t, abfluss = get_info()


  f = open("time.txt", "a")
  f.write(time.asctime())
  f.write("\n")
  f.close()
  f2 = open("abfluss_mellingen.txt", "a")
  f2.write(t)
  f2.write(" ")
  f2.write(abfluss)
  f2.write("\n")
  f2.close()