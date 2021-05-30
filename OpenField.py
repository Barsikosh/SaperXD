class Field:

    def __init__(self,array,x,y):
        self.array = array.copy()
        self.lenX = len(self.array[0])
        self.lenY = len(self.array)
        self.x = x
        self.y = y
##----------------------------------        
    def check_bombs(self,y,x):
        for dx in  range(-1,2):
            for dy in range(-1,2):
                if(not ((x+dx<0) or (y+dy<0) or (x+dx>=self.lenX) or (y+dy>=self.lenY))):
                    if self.array[x+dx][y+dy] == 'b':
                        return True
        return False
##----------------------------------     
    def open_cell(self,y,x):
        if ((x<0) or (y<0) or (x>=self.lenX) or (y>=self.lenY)):
            return
        if self.array[x][y] == 1:
            return
        self.array[x][y] = 1
        self.open_neighbor(x,y)
        
##----------------------------------     
    def open_neighbor(self,y,x):
        if (self.check_bombs(x,y)):
            return
        for dx in  range(-1,2):
            for dy in range(-1,2):
                if ((dx == 0) and (dy == 0)):
                    continue
                self.open_cell(x+dx,y+dy)
##----------------------------------         
