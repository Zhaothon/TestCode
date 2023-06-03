class block:
    t_b=False
    r_b=False
    b_b=False
    l_b=False
    nane=""
    def __init__(self,loca):
        self.name=loca
    def chbd(self,side):
        if side == "top":
            if self.t_b:
                self.t_b=True
            else:
                self.t_b=False
        elif side == "right":
            if self.r_b:
                self.r_b=True
            else:
                self.r_b=False
        elif side == "bottom":
            if self.b_b:
                self.b_b=True
            else:
                self.b_b=False
        elif side == "left":
            if self.l_b:
                self.l_b=True
            else:
                self.l_b=False
        else:
            warn(0)
    def bdlist(self,bd="all"):
        t=int(self.t_b)
        r=int(self.r_b)
        b=int(self.b_b)
        l=int(self.l_b)
        if bd == "all":
            return [t,r,b,l]
        elif bd == "top":
            return [t]
        elif bd == "right":
            return [r]
        elif bd == "bottom":
            return [b]
        elif bd == "left":
            return [l]
        else:
            warn(1)

def warn(code):
    if code == 1:
        pass

a=[]
a.append(block("1"))