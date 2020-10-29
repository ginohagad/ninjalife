#!/usr/bin/env python3

import pygame as pg
import sys
import os
import time

pg.font.init()

WIN_SIZE= WIDTH, HEIGHT = 1040, 750

WINDOW = pg.display.set_mode(WIN_SIZE)
pg.display.set_caption('Ninja Life')

NINJA = pg.image.load(os.path.join('png', 'Attack__000.png'))
NINJARECT = NINJA.get_rect()

BG = pg.transform.scale(pg.image.load(os.path.join('png', 'bg-forest.png')), WIN_SIZE)

class Player(pg.sprite.Sprite):
  def __init__(self, x, y):
    super(Player, self).__init__()
    self.x = x
    self.y = y
    self.player_img = pg.transform.scale(NINJA, (200, 230))

    self.run = []
    self.run.append(pg.image.load('png/Run__000.png'))
    self.run.append(pg.image.load('png/Run__001.png'))
    self.run.append(pg.image.load('png/Run__002.png'))
    self.run.append(pg.image.load('png/Run__003.png'))
    self.run.append(pg.image.load('png/Run__004.png'))
    self.run.append(pg.image.load('png/Run__005.png'))
    self.run.append(pg.image.load('png/Run__006.png'))
    self.run.append(pg.image.load('png/Run__007.png'))
    self.run.append(pg.image.load('png/Run__008.png'))
    self.run.append(pg.image.load('png/Run__009.png'))

    self.index = 0
    self.player_img = pg.transform.scale(NINJA, (200, 230))
    
    # self.player_img = self.run[self.index]
    # self.rect = self.player_img.get_rect()


  def draw(self, win):
    win.blit(self.player_img, (self.x, self.y))

  def get_width(self):
    return self.player_img.get_width()

  def get_height(self):
    return self.player_img.get_height()

  def update(self):
    pass

  def player_run(self):
    self.index += 1
    if self.index >= len(self.run):
      self.index = 0
    # self.player_img = self.run[self.index]
    self.player_img = pg.transform.scale(self.run[self.index], (200, 230))

  def player_stand(self):
    self.player_img = pg.transform.scale(NINJA, (200, 230))


def main():
  running = True
  FPS = 60
  main_font = pg.font.SysFont('comicsans', 50)
  vel = 5
  is_jump = False
  jump_count = 10
  run_count = 0

  player = Player(100, 500)
  group = pg.sprite.Group(player)

  clock = pg.time.Clock()


  while running:
    clock.tick(FPS)
    WINDOW.blit(BG, (0, 0))

    player.draw(WINDOW)
    pg.display.update()

    for event in pg.event.get():
      if event.type == pg.KEYDOWN:
        if (event.key == pg.K_ESCAPE) or (event.type == pg.QUIT):
          running = False
      else:
        player.player_stand()


    keys = pg.key.get_pressed()
    if keys[pg.K_a] and player.x - vel > 0:
      player.x -= vel
      player.player_run()

    if keys[pg.K_d] and player.x + vel + player.get_width() < WIDTH:
      player.x += vel
      player.player_run()

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
