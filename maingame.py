from pico2d import *
import os
head_width = 45
head_height = 42
body_width = 29
body_height = 25
frame = 0
Tile_Size = 100
playing = True
open_canvas()



def locatetile():
    for i in range(48):
        if Tiles[i].x == 0:
            Tiles[i].image = load_image('tileleft.png')
        if Tiles[i].x == 7:
            Tiles[i].image = load_image('tileright.png')
        if Tiles[i].y == 0:
            if Tiles[i].x == 0:
                Tiles[i].image = load_image('tileld.png')
            elif Tiles[i].x == 7:
                Tiles[i].image = load_image('tilerd.png')
            else:
                Tiles[i].image = load_image('tilebot.png')
        if Tiles[i].y == 5:
            if Tiles[i].x == 0:
                Tiles[i].image = load_image('tilelu.png')
            elif Tiles[i].x == 7:
                Tiles[i].image = load_image('tileru.png')
            else:
                Tiles[i].image = load_image('tiletop.png')

        if Tiles[i].y==3:
            if Tiles[i].x==7:

                Tiles[i].image=load_image('dooropen.png')

def handle_events():
    global GamePlay
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            GamePlay = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_a:
                Body.direction = 1
                Head.frame = 7
            elif event.key == SDLK_d:
                Body.direction = 2
                Head.frame = 3
            elif event.key == SDLK_w:
                Body.direction = 3
                Head.frame = 5
            elif event.key == SDLK_s:
                Body.direction = 4
                Head.frame = 1
                if event.key == SDLK_LEFT:
                    Head.frame = 7
                    if ball[0].appear==False:
                        ball[0].appear=True
                        ball[0].x=Head.x
                        ball[0].y=Head.y
                        ball[0].dir=1
                        ball[0].speed=0


                elif event.key == SDLK_RIGHT:
                    Head.frame = 3
                    if ball[1].appear==False:
                        ball[1].appear=True
                        ball[1].x=Head.x
                        ball[1].y=Head.y
                        ball[1].dir=2
                        ball[1].speed=0

                elif event.key == SDLK_UP:
                    Head.frame = 5
                    if ball[2].appear==False:
                        ball[2].appear=True
                        ball[2].x=Head.x
                        ball[2].y=Head.y
                        ball[2].dir=3
                        ball[2].speed=0
                elif event.key == SDLK_DOWN:
                    Head.frame = 1
                    if ball[3].appear==False:
                        ball[3].appear=True
                        ball[3].x=Head.x
                        ball[3].y=Head.y
                        ball[3].dir=4
                        ball[3].speed=0

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_a or SDLK_d or SDLK_w or SDLK_s:
                Body.direction = 0
                if event.key == SDLK_LEFT:
                    Head.frame = 6
                elif event.key == SDLK_RIGHT:
                    Head.frame = 2
                elif event.key == SDLK_UP:
                    Head.frame = 4
                elif event.key == SDLK_DOWN or SDLK_w:
                    Head.frame = 0



os.chdir('C:/Users/서정원/Desktop/GIT/Project2dgp/resources')

class Body:
    def __init__(self):
        self.image = load_image('Bodysheet.png')
        self.frame = 0
        self.x = 400
        self.y = 300
        self.direction = 0                      # 0 = 가만히, 1 = 왼쪽, 2 = 오른쪽, 3 = 위쪽, 4 = 밑쪽
    def update(self):
        if self.direction == 0:
            self.frame = 0
        else:
            self.frame = (self.frame + 1) % 10
            if self.direction == 1 and (self.x>45):
                self.x -= 10
            elif self.direction == 2 and (self.x<755):
                self.x += 10
            elif self.direction == 3 and (self.y<555):
                self.y += 10
            if self.direction == 4 and (self.y>45):
                self.y -= 10

    def draw(self):

        if self.direction == 0:
            self.image.clip_draw(self.frame * body_width, 50, body_width, body_height, self.x,
                                 self.y)
        elif self.direction >= 3:
            self.image.clip_draw(self.frame * body_width, 50, body_width, body_height, self.x, self.y)
        elif self.direction==1:
            self.image.clip_draw(self.frame * body_width, 0 , body_width, body_height, self.x,
                                 self.y)
        elif self.direction==2:
            self.image.clip_draw(self.frame * body_width, 25 , body_width, body_height, self.x,
                                 self.y)


Body = Body()
class ball:
    def __init__(self):
        ball.image=load_image('ball.png')
        self.x=Head.x
        self.y=Head.y
        self.dir=0
        self.speed=0
        self.appear=False
    def locate(self):
        return self.x-10,self.y-10,self.x+10,self.y+10
    def draw(self):
        if self.appear==True:
            self.image.clip_draw(0,0,10,10,self.x,self.y)
        pass
    def update(self):
        if self.appear==True:
            if self.dir==1:
                self.x-=15+self.speed
            elif self.dir==2:
                self.x+=15+self.speed
            elif self.dir==3:
                self.y+=15+self.speed
            elif self.dir==4:
                self.y-=15+self.speed
        else:
            self.x=Head.x
            self.y=Head.y
            self.speed-=0.4
            if self.speed<-15:
                self.appear=False
    def stop(self):
        pass
class Head:


    def __init__(self):
        self.image = load_image('Headsheet.png')
        self.frame = 0
        self.x = Body.x
        self.y = Body.y + 25


    def update(self):
        self.x = Body.x
        self.y = Body.y + 25

    def draw(self):
        self.image.clip_draw(self.frame * head_width, 0, head_width, 42, self.x, self.y) #머리 세로 길이 45 머리 가로 길이 42

class Tile:
    def __init__(self):
        self.x = 1
        self.y = 1
        self.image = load_image('tile_mid.png')

    def Draw(self):

        if(self.x==7 and self.y==3):
            self.image.clip_draw(0, 0, Tile_Size, 105, self.x * 100 + 50, self.y * 100 + 47)
        # if(self.x==7 and self.y==2):
        #     self.image.clip_draw(0, 0, Tile_Size, 105, self.x * 100 + 50, self.y * 100 + 53)
        else:
            self.image.clip_draw(0, 0, Tile_Size, Tile_Size, self.x * 100 + 50, self.y * 100 + 50)
Head = Head()
Tiles = [Tile() for i in range(0, 48)]
ball=[ball() for i in range(4)]
for i in range(0, 48):
    Tiles[i].x = i % 8
    Tiles[i].y = i // 8
    locatetile()

while playing:
    Body.update()
    Head.update()
    clear_canvas()
    for i in range(48):
        Tiles[i].Draw()
    for i in range(4):
        ball[i].update()
    Body.draw()
    Head.draw()
    for i in range(4):
        ball[i].draw()
    update_canvas()
    handle_events()
    delay(0.05)
close_canvas()