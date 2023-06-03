"""
A New Game
For learning
Class
"""
int("a")

class Block:
    """
    base game object:
    Block
    Just like a square in a map
    """
    t_b=False
    r_b=False
    b_b=False
    l_b=False
    nane=""
    def __init__(self,loca):
        self.name=loca
    def chbd(self,side):
        """
        Set walls
        At the side of Block
        """
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
    def bdlist(self,border="all"):
        """
        show the walls
        of a Block
        """
        top=int(self.t_b)
        right=int(self.r_b)
        bottom=int(self.b_b)
        left=int(self.l_b)
        if border == "all":
            return [top,right,bottom,left]
        elif border == "top":
            return top
        elif border == "right":
            return right
        elif border == "bottom":
            return bottom
        elif border == "left":
            return left
        else:
            #warn(1)
            pass

def warn(code):
    """
    warn programmer to
    use Block properly -- ToDo
    """
    if code == 1:
        pass
    else:
        pass

class BlockBox:
    """
    base game object:
    BlockBox
    just like a map
    """
    a=[]
    size_x=0
    size_y=0
    def __init__(self,x_len=5,y_len=5):
        self.size_x=x_len
        self.size_y=y_len
        for i in range(x_len):
            for j in range(y_len):
                self.a.append(Block(str(i+1)+str(j+1)))

#test
test=BlockBox()
