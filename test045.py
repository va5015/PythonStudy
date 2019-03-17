import time
import mylib
import mypackage.mylib

time.sleep(1)
ret1= mylib.add_txt('나는','파이썬이다')
mypackage.mylib.reverse(1,2,3)

print(ret1)