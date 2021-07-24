import pyglet
from pyglet import image
from pyglet.sprite import Sprite

class Button:
    def __init__(self,x,y,w,h,on,off,text,type):
        self.w, self.h = w, h
        self.x,self.y = x-self.w//2,y-self.h//2
        self.imgs = [image.load(off),image.load(on)]
        self.on = False
        self.sprite = Sprite(self.imgs[0])
        self.sprite.x = x - self.w//2
        self.sprite.y = y - self.h//2
        self.sprite.scale_x = self.w/910
        self.sprite.scale_y = self.h/290
        self.type = type
        self.lab = pyglet.text.Label(text,
                          font_name='Arial',
                          font_size=15,
                          x=self.x+self.w//2-len(text)*6, y=self.y+self.h//2-6)

    def draw(self,args):
        self.sprite.image = self.imgs[int(self.on)]
        self.sprite.draw()
        self.lab.draw()

    # x,y,(1,0,-1),func,arguments
    def isHit(self,args):
        x = args[0]
        y = args[1]
        b = args[2]
        o = args[3]
        args = args[4]
        if b == 1:
            if x > self.x and x < self.x + self.w:
                if y > self.y and y < self.y + self.h:
                    self.on = True
                    self.draw()
                    self.run(o,args)
        elif b == -1:
            if x > self.x and x < self.x + self.w:
                if y > self.y and y < self.y + self.h:
                    self.on = False
        elif b == 0:
            z = 1
            if x > self.x and x < self.x + self.w:
                if y > self.y and y < self.y + self.h:
                    self.on = True
                    z = 0
            if z == 1:
                self.on = False

    def run(self,f,args):
        f(args)