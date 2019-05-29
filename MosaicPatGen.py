import random
import time
from turtle import *
from graphics import *

WINDOWS = True

class Gravity:
    def __init__(self, x_, y_):
        self.x = x_
        self.y = y_

class Pixel:
    def __init__(self, value_):
        self.value = value_

class Matrix:
    pixel = {}
    max_x = 0
    max_y = 0
    Gravities=[]

    def __init__(self, x_, y_):
        self.max_x = x_
        self.max_y = y_
        self.pixel = [[0 for y in range(y_+1)] for x in range(x_+1)] 
        x = 0
        y = 0
        print("Hello")
        while y < y_:
            y+=1
            while x < x_:
                x+=1
                self.pixel[x][y] = 0

    def AddGravity(self, gravity_):
        self.Gravities.append(gravity_)

    def Dump(self):
        y = 0
        while (y < self.max_y):
            y+=1
            x = 0
            s = ""
            while (x < self.max_x):
                x += 1
                s += str(self.pixel[x][y]).rjust(1) + " "
            if not y % 2 :
                s = ' ' + s
            print(s)

    def Distance(self, x_, y_):
        res = 9999999999
        for G in self.Gravities:
            diffX = abs(G.x - x_)
            diffY = abs(G.y - y_)
            r = diffX + diffY
            if(r<res):
                res = r
        return res

    def CalcDistance(self):
        y = 0
        while (y < self.max_y):
            y+=1
            x = 0
            while (x < self.max_x):
                x += 1
                self.pixel[x][y] = self.Distance(x, y)
    
    def AddNoise(self, level):
        y = 0
        while (y < self.max_y):
            y+=1
            x = 0
            while (x < self.max_x):
                x += 1
                noise =  random.randrange(-(level), level, 1)
                noise -= (level/2)
                self.pixel[x][y] += noise

    def BlackWhite(self, treshold):
        y = 0
        while (y < self.max_y):
            y+=1
            x = 0
            while (x < self.max_x):
                x += 1
                if x%10!=0:
                    if self.pixel[x][y] > treshold:
                        self.pixel[x][y] = 'x'
                    else:
                        self.pixel[x][y] = '.'
                else:
                    if self.pixel[x][y] < treshold:
                        if random.randrange(0,2) == 0:
                            self.pixel[x][y] = '.'
                        else:
                            self.pixel[x][y] = 'x'
                    else:
                        self.pixel[x][y] = 'x'
                        
                
    def PaintHex(self, x, y, size, bw):
        corners = 6
        angle = 360/corners
        cnt = corners
        if bw == '.':
            color("black","white")
        else:
            color("black","black")
        begin_fill()
        setpos(x,y)
        pendown()
        #left(angle)
        while cnt > 0:
            cnt-=1
            forward(size)
            right(angle)
        #right(angle)
        end_fill()
        penup()

    def PaintInit(self):
        print("init x")
        speed(0)
        penup()
        
    def PaintInit_win(self):
        print("init win")
        self.win = GraphWin("My Circle", 1000, 750)

    def PaintEnd_win(self):
        print("end win")
        self.win.getMouse() # Pause to view result
        self.win.close()    # Close window when done

    def PaintHex_win(self, x, y, size, bw):
        c = Circle(Point(x+10,y+10), size)
        if bw == 'x':
            c.setFill('black')
        c.draw(self.win)

    def Paint(self):
        if WINDOWS:
            self.PaintInit_win()
        else:
            self.PaintInit()
        posX = 0
        posY = 0
        size = 4
        space = 2
        y = 0
        while (y < self.max_y):
            y+=1
            x = 0
            while (x < self.max_x):
                x += 1
                if WINDOWS:
                    self.PaintHex_win(posX, posY, size, self.pixel[x][y])
                else:
                    self.PaintHex(posX, posY, size, self.pixel[x][y])
                
                posX += (size*3) + space
#                self.pixel[x][y] = '.'
            posY += (size)
            offset = 0
            if y % 2 :
                offset = size*1.5 + space/2
            posX = offset
        if WINDOWS:
            self.PaintEnd_win()

if __name__ == "__main__":
    M = Matrix(50, 120)
    M.AddGravity(Gravity(0,1))
    #M.AddGravity(Gravity(5,1))
    #M.AddGravity(Gravity(10,1))
    #M.AddGravity(Gravity(15,1))
    #M.AddGravity(Gravity(20,1))
    M.AddGravity(Gravity(25,1))
    M.AddGravity(Gravity(50,1))
    M.AddGravity(Gravity(49,49))

    M.AddGravity(Gravity(25,100))

    M.CalcDistance()
    #M.Dump()

    print("---")
    M.AddNoise(15) #8
    #M.Dump()

    print("---")
    M.BlackWhite(10) #8
    M.Dump()

    M.Paint()
 
#    input("Press Enter to continue...")
