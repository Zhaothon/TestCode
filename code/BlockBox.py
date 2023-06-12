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
    filled=False
    loca=Loca(1,1)
    def __init__(self,loca,fill=False):
        self.loca=loca
        self.filled=fill
    def fill_status(self):
        return self.filled
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
