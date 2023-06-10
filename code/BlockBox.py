"""
A New Game
For learning
Class
"""
class Loca:
    x=0
    y=0
    def __init__(self,m=0,n=0):
        self.x=m
        self.y=n

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
    loca=[]
    def __init__(self,loca_x,loca_y):
        m=[loca_x,loca_y]
        self.loca=m
        del m
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
    block_group=[]
    block_name=[]
    size_x=0
    size_y=0
    def __init__(self,x_len=5,y_len=5):
        self.size_x=x_len
        self.size_y=y_len
        for i in range(x_len):
            for j in range(y_len):
                self.block_group.append(Block(i+1,j+1))
                self.block_name.append([i+1,j+1])
        del i,j

    def choose_block(self,x_loca,y_loca):
        """
        provide API
        to operate
        Block
        """
        counter=0
        for i in self.block_name:
            if i[0] == x_loca:
                if i[1] == y_loca:
                    return self.block_group[counter]
                else:
                    counter+=1
            else:
                counter+=1
        return None
    def choose_blocks(self,x_start,x_end,y_start,y_end):
        """
        based on 
        'choose_block':
        choose many blocks
        """
        target_x=[]
        target_y=[]
        targets=[]
        returns=[]
        for i in range(x_end):
            if (i+1) >= x_start:
                target_x.append(i+1)
        #test point:
        #print(target_x)
        #end test!
        del i
        for i in range(y_end):
            if (i+1) >= y_start:
                target_y.append(i+1)
        del i
        for i in target_x:
            for j in target_y:
                targets.append([i,j])
        del i,j,target_x,target_y
        for i in targets:
            returns.append(self.choose_block(i[0],i[1]))
        del i,targets
        return returns
