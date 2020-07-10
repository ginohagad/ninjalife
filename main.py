#!/usr/bin/env python3

import pygame as pg
import os
import time

pg.font.init()

win_size = WIDTH, HEIGHT = 1040, 750

window = pg.display.set_mode(win_size)
pg.display.set_caption('Ninja Life')

NINJA = pg.image.load(os.path.join('png', 'Attack__002.png'))
NINJARECT = NINJA.get_rect()

BG = pg.transform.scale(pg.image.load(os.path.join('png', 'bg-forest.png')), win_size)


class Player:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.player_img = pg.transform.scale(NINJA, (200, 230))
    self.run = [pg.image.load(os.path.join('png', f'Run__00{x}' + '.png')) for x in range(0,9)]
    self.rect = self.player_img.get_rect()

  def draw(self, win):
    win.blit(self.player_img, (self.x, self.y))

  def get_width(self):
    return self.player_img.get_width()

  def get_height(self):
    return self.player_img.get_height()

def main():
  running = True
  FPS = 60
  main_font = pg.font.SysFont('comicsans', 50)
  vel = 5
  is_jump = False
  jump_count = 10

  player = Player(100, 500)

  clock = pg.time.Clock()


  while running:
    clock.tick(FPS)
    window.blit(BG, (0, 0))

    player.draw(window)
    pg.display.update()

    for event in pg.event.get():
      if event.type == pg.QUIT:
        running = False


    keys = pg.key.get_pressed()
    if keys[pg.K_a] and player.x - vel > 0:
      player.x -= vel

    if keys[pg.K_d] and player.x + vel + player.get_width() < WIDTH:
      player.x += vel

    if not is_jump:
      if keys[pg.K_SPACE]:
        is_jump = True
    else:
      if jump_count >= -10:
        player.y -= (jump_count * abs(jump_count)) * 0.9
        jump_count -= 1
      else:
        jump_count = 10
        is_jump = False


if __name__=='__main__':
  main()
