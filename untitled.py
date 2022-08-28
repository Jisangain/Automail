from time import time, sleep
def loading(flag):
    for x in range (0,30):  
        b = "Loading" + "." * x
        print (b, end="\r")
        sleep(.5)
loading(True)
print(" "*36,end="\b")