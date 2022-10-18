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
        if Tiles[i].y==2:
            if Tiles[i].x==7:
                Tiles[i].image=load_image('doorclose.png')

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

                elif event.key == SDLK_RIGHT:
                    Head.frame = 3

                elif event.key == SDLK_UP:
                    Head.frame = 5

                elif event.key == SDLK_DOWN:
                    Head.frame = 1

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
            if self.direction == 1:
                self.x -= 7
            elif self.direction == 2:
                self.x += 7
            elif self.direction == 3:
                self.y += 7
            elif self.direction == 4:
                self.y -= 7

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
        self.image.clip_draw(0, 0, Tile_Size, Tile_Size, self.x * 100 + 50, self.y * 100 + 50)


Head = Head()
Tiles = [Tile() for i in range(0, 48)]

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

    Body.draw()
    Head.draw()
    update_canvas()
    handle_events()
    delay(0.05)
close_canvas()