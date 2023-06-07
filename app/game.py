import time as t,random as r
RAN=0
a=[]
def ranum(min,max):
    global RAN
    RAN=r.randint(min,max)

def intput():
    a=input("min>")
    b=input("max>")
    if tryint(a):
        if tryint(b):
            return [int(a),int(b)]
        else:
            warn(1)
    else:
        warn(2)
    return [0,0]

def tryint(n):
    try:
        n=int(n)
    except BaseException:
        return False
    else:
        return True

def warn(code):
    if code == 1:
        print("'max' is not a number!")
    elif code == 2:
        print("'min' is not a number!")
    else:
        pass

input()
