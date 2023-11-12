import pygame as pg
import random as rnd
from dataclasses import dataclass

pg.init()   
width, columns, rows = 700, 30, 20
distance = width // columns
height = distance * rows
grid = [0] * columns * rows
tet=[4]
picture = [] 
for n in range(8):
  picture.append(pg.transform.scale(pg.image.load(f'T_{n}.gif'), (distance, distance)))
screen = pg.display.set_mode([width, height])
pg.display.set_caption('knights_Quest')
tetroromino[1]=4
grid[160]=2                                     
grid[161]=2
grid[162]=2
grid[163]=2
grid[164]=2
grid[165]=2
grid[166]=2
grid[167]=2
grid[168]=2
grid[169]=2
grid[170]=2
grid[171]=2
grid[172]=2
grid[300]=2
grid[301]=2
grid[302]=2
grid[303]=2
grid[304]=2
grid[305]=2
grid[306]=2
grid[307]=2
grid[308]=2
grid[309]=2
grid[310]=2
@dataclass
class tetroromino():
    tetro: list
    row: int = 0 # vị trí xuất hiện đầu tiên
    column: int = 5



status = True
while status:
    pg.time.delay(10)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            status = False
    screen.fill((128,128,128))

    for n, color in enumerate(grid): # enumerate tạo list dạng liệt kê
        if color > 0:
            x= n % columns * distance
            y= n // columns * distance
            screen.blit(picture[color],(x,y))
    pg.display.flip()
  
pg.quit()