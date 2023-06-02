import time as t,random as r
RAN=0
a=[]
def ranum(min,max):
    global RAN
    RAN=r.randint(min,max)

def intput():
    a=input("min>")
    b=input("max>")