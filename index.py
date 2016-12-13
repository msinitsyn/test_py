#! C:/Users/msini/AppData/Local/Programs/Python/Python35-32/python.exe

import test

print("Content-Type: text/html\n")
print("<html><head><title>Parser table</title></head><body>")
dat = test.parser()
datHtm = test.table(dat)
print(datHtm)
print("</body></html>")
