"""
一个用于游戏的网格模型
"""
class Loca:
    """
    用于描述位置
    """
    x_loca=0
    y_loca=0
    def __init__(self,new_x=0,new_y=0):
        self.x_loca=new_x
        self.y_loca=new_y

class Block:
    """
    用于描述并更改网格状态
    """
    filled=False
    loca=Loca(1,1)
    def __init__(self,loca=Loca(0,0),fill=False):
        self.loca=loca
        self.filled=fill
    def fill_status(self):
        """
        whether a Block
        is full
        """
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
        locas=[]
        for i in range(x_len):
            for j in range(y_len):
                locas.append(Loca(i+1,j+1))
                self.block_name.append([i+1,j+1])
        del i,j
        for k in locas:
            self.block_group.append(Block(k))

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
        del target_x,target_y
        for k in targets:
            returns.append(self.choose_block(k[0],k[1]))
        del targets
        return returns
