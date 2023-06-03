class Block:
    t_b=False
    r_b=False
    b_b=False
    l_b=False
    loca=""
    def __init__(self,loca):
        self.loca=loca
    def chside(self,side):
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
    def border_list(self,side="all"):
        top=int(self.t_b)
        right=int(self.r_b)
        bottom=int(self.b_b)
        left=int(self.l_b)
        if side == "all":
            return [top,right,bottom,left]
        elif side == "top":
            return top
        elif side == "right":
            return right
        elif side == "bottom":
            return bottom
        elif side == "left":
            return left

class BlockBox:
    a=1
    
