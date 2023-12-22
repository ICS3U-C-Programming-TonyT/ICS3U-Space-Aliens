#!/usr/bin/env python3

# Created Tony Tran
# Created December 22, 2023
# This is the code for Capybara Catcher

import random
import time

import constants
import stage
import supervisor
import ugame

# Settings
#  Audio
COIN_SOUND_SETTING = constants.COIN_SOUND_SETTING
BOOM_SOUND_SETTING = constants.BOOM_SOUND_SETTING
CRASH_SOUND_SETTING = constants.CRASH_SOUND_SETTING
PEW_SOUND_SETTING = constants.PEW_SOUND_SETTING

<<<<<<< HEAD
#  Images
IMAGE_BANK_MT_BACKGROUND_SETTING = constants.IMAGE_BANK_MT_BACKGROUND_SETTING
IMAGE_BANK_BACKGROUND_SETTING = constants.IMAGE_BANK_BACKGROUND_SETTING
IMAGE_BANK_SPRITES_SETTING = constants.IMAGE_BANK_SPRITES_SETTING

def splash_scene():
  # this function is the splash scene

  # sound prep
  coin_sound = open(COIN_SOUND_SETTING, "rb")
  sound = ugame.audio
  sound.stop()
  sound.mute(False)
  sound.play(coin_sound)

  # image banks
  image_bank_mt_background = stage.Bank.from_bmp16(IMAGE_BANK_MT_BACKGROUND_SETTING)

  # sets the background to image 0 in the bank
  background = stage.Grid(image_bank_mt_background, constants.SCREEN_X,
                          constants.SCREEN_Y)

  # mt logo tiles
  background.tile(2, 2, 0)  # blank white
  background.tile(3, 2, 1)
  background.tile(4, 2, 2)
  background.tile(5, 2, 3)
  background.tile(6, 2, 4)
  background.tile(7, 2, 0)  # blank white

  background.tile(2, 3, 0)  # blank white
  background.tile(3, 3, 5)
  background.tile(4, 3, 6)
  background.tile(5, 3, 7)
  background.tile(6, 3, 8)
  background.tile(7, 3, 0)  # blank white

  background.tile(2, 4, 0)  # blank white
  background.tile(3, 4, 9)
  background.tile(4, 4, 10)
  background.tile(5, 4, 11)
  background.tile(6, 4, 12)
  background.tile(7, 4, 0)  # blank white

  background.tile(2, 5, 0)  # blank white
  background.tile(3, 5, 0)
  background.tile(4, 5, 13)
  background.tile(5, 5, 14)
  background.tile(6, 5, 0)
  background.tile(7, 5, 0)  # blank white

  # creates a stage, sets to 60fps
  game = stage.Stage(ugame.display, constants.FPS)
  # order of layers
  game.layers = [background]
  # render the background and sprite list, most likely once per scene
  game.render_block()

  # repeat forever, game loop
  while True:
    # wait 2 seconds
    time.sleep(2.0)
    menu_scene()


def menu_scene():
  # this function is the main menu scene
=======
def menu_scene():
    # this function is the menu scene
>>>>>>> fa8497a8c1f4c58a15dcbcbf7cdaab58ab0b1930

  # image banks
  image_bank_background = stage.Bank.from_bmp16(IMAGE_BANK_MT_BACKGROUND_SETTING)

  # add text objects
  text = []
  text1 = stage.Text(width=29,
                     height=12,
                     font=None,
                     palette=constants.RED_PALETTE,
                     buffer=None)
  text1.move(20, 10)
  text1.text("Capybara Catcher")
  text.append(text1)

  text2 = stage.Text(width=29,
                     height=12,
                     font=None,
                     palette=constants.RED_PALETTE,
                     buffer=None)
  text2.move(40, 110)
  text2.text("PRESS START")
  text.append(text2)

  # sets the background, 10x8
  background = stage.Grid(image_bank_background, constants.SCREEN_X,
                          constants.SCREEN_Y)

  # creates a stage, sets to 60fps
  game = stage.Stage(ugame.display, constants.FPS)
  # order of layers
  game.layers = text + [background]
  # render the background and sprite list, most likely once per scene
  game.render_block()

  # repeat forever, game loop
  while True:
    # get user input
    keys = ugame.buttons.get_pressed()

    if keys & ugame.K_START != 0:
      game_scene()

<<<<<<< HEAD
    # redraw Sprites
    game.tick()
=======
    while True:
        # settings options
        options = {
            1: "start",
            2: "instructions",
        }
        # get user input
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_UP != 0:
            if select == options[1]:
                pass
            else:
                select = options[1]
                start_text.text("> START <")
                instruction_text.text("INSTRUCTIONS")
                
        if keys & ugame.K_DOWN != 0:
            if select == options[2]:
                pass
            else:
                select = options[2]
                instruction_text.text("> INSTRUCTIONS <")
                start_text.text("START")

        if keys & ugame.K_START != 0:
            game_scene()

        # redraw sprites
        game.render_block()
        game.tick()
>>>>>>> fa8497a8c1f4c58a15dcbcbf7cdaab58ab0b1930


def game_scene():
  # this function is the main game game_scene

  # for score
  score = 0

  score_text = stage.Text(width=29, height=14)
  score_text.clear()
  score_text.cursor(0, 0)
  score_text.move(1, 1)
  score_text.text("Score: {0}".format(score))

  def show_alien():
    # this function takes an alien from off screen and moves it on
    for alien_number in range(len(aliens)):
      if aliens[alien_number].x < 0:
        aliens[alien_number].move(
            random.randint(
                0 + constants.SPRITE_SIZE,
                constants.SCREEN_X - constants.SPRITE_SIZE,
            ),
            constants.OFF_TOP_SCREEN,
        )
        break

  # image banks
  image_bank_background = stage.Bank.from_bmp16(IMAGE_BANK_MT_BACKGROUND_SETTING)
  image_bank_sprites = stage.Bank.from_bmp16(IMAGE_BANK_SPRITES_SETTING)

  # button state info
  a_button = constants.button_state["button_up"]
  b_button = constants.button_state["button_up"]
  start_button = constants.button_state["button_up"]
  select_button = constants.button_state["button_up"]

  # get sound ready
  pew_sound = open(PEW_SOUND_SETTING, "rb")
  boom_sound = open(BOOM_SOUND_SETTING, "rb")
  crash_sound = open(CRASH_SOUND_SETTING, "rb")
  sound = ugame.audio
  sound.stop()
  sound.mute(False)

  # sets the background, 10x8
  background = stage.Grid(image_bank_background, constants.SCREEN_X,
                          constants.SCREEN_Y)
  for x_location in range(constants.SCREEN_GRID_X):
    for y_location in range(constants.SCREEN_GRID_Y):
      tile_picked = random.randint(1, 3)
      background.tile(x_location, y_location, tile_picked)

  ship = stage.Sprite(image_bank_sprites, 5, 75,
                      constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))

  # create list of aliens
  aliens = []
  for alien_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
    a_single_alien = stage.Sprite(image_bank_sprites, 9,
                                  constants.OFF_SCREEN_X,
                                  constants.OFF_SCREEN_Y)
    aliens.append(a_single_alien)

  # place 1 alien on the screen
  show_alien()

  # create list of lasers when we shoot
  lasers = []
  for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
    a_single_laser = stage.Sprite(image_bank_sprites, 10,
                                  constants.OFF_SCREEN_X,
                                  constants.OFF_SCREEN_Y)
    lasers.append(a_single_laser)

  # creates a stage, sets to 60fps
  game = stage.Stage(ugame.display, 60)
  # order of layers
  game.layers = [score_text] + lasers + [ship] + aliens + [background]
  # render the background and sprite list, most likely once per scene
  game.render_block()

  # repeat forever, game loop
  while True:
    # get user input
    keys = ugame.buttons.get_pressed()

    if keys & ugame.K_O != 0:
      if a_button == constants.button_state["button_up"]:
        a_button = constants.button_state["button_just_pressed"]
      elif a_button == constants.button_state["button_just_pressed"]:
        a_button = constants.button_state["button_still_pressed"]

    else:
      if a_button == constants.button_state["button_still_pressed"]:
        a_button = constants.button_state["button_released"]
      else:
        a_button = constants.button_state["button_up"]

    if keys & ugame.K_RIGHT != 0:
      if ship.x < (constants.SCREEN_X - constants.SPRITE_SIZE):
        ship.move((ship.x + constants.SPRITE_MOVEMENT_SPEED), ship.y)
      else:
        ship.move((constants.SCREEN_X - constants.SPRITE_SIZE), ship.y)

    if keys & ugame.K_LEFT != 0:
      if ship.x > 0:
        ship.move((ship.x - constants.SPRITE_MOVEMENT_SPEED), ship.y)
      else:
        ship.move(0, ship.y)

    if keys & ugame.K_UP != 0:
      ship.move(ship.x, ship.y - 1)
    if keys & ugame.K_DOWN != 0:
      ship.move(ship.x, ship.y + 1)

    # update game logic
    # play sound on A being pressed
    if a_button == constants.button_state["button_just_pressed"]:
      # fire a laser, if limit is not exceeded
      for laser_number in range(len(lasers)):
        if lasers[laser_number].x < 0:
          lasers[laser_number].move(ship.x, ship.y)
          sound.play(pew_sound)
          break

    # each frame move the lasers that have been fired up
    for laser_number in range(len(lasers)):
      if lasers[laser_number].x > 0:
        lasers[laser_number].move(
            lasers[laser_number].x,
            lasers[laser_number].y - constants.LASER_SPEED,
        )
      if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
        lasers[laser_number].move(constants.OFF_SCREEN_X,
                                  constants.OFF_SCREEN_Y)

    # each frame moves the aliens down
    for alien_number in range(len(aliens)):
      if aliens[alien_number].x > 0:
        aliens[alien_number].move(
            aliens[alien_number].x,
            aliens[alien_number].y + constants.ALIEN_SPEED,
        )
      if aliens[alien_number].y > constants.SCREEN_Y:
        aliens[alien_number].move(constants.OFF_SCREEN_X,
                                  constants.OFF_SCREEN_Y)
        show_alien()
        score -= 1
        if score < 0:
          score = 0
        score_text.clear()
        score_text.cursor(0, 0)
        score_text.move(1, 1)
        score_text.text("Score: {0}".format(score))

    # each frame check if any of the lasers are touching any of the aliens
    for laser_number in range(len(lasers)):
      if lasers[laser_number].x > 0:
        for alien_number in range(len(aliens)):
          if aliens[alien_number].x > 0:
            if stage.collide(
                lasers[laser_number].x + 6,
                lasers[laser_number].y + 2,
                lasers[laser_number].x + 11,
                lasers[laser_number].y + 12,
                aliens[alien_number].x + 1,
                aliens[alien_number].y,
                aliens[alien_number].x + 15,
                aliens[alien_number].y + 15,
            ):
              # alien hit
              aliens[alien_number].move(constants.OFF_SCREEN_X,
                                        constants.OFF_SCREEN_Y)
              lasers[laser_number].move(constants.OFF_SCREEN_X,
                                        constants.OFF_SCREEN_Y)
              boom_sound = open(BOOM_SOUND_SETTING, "rb")
              sound.stop()
              sound.play(boom_sound)
              show_alien()
              show_alien()
              score = score + 1
              score_text.clear()
              score_text.cursor(0, 0)
              score_text.move(1, 1)
              score_text.text("Score: {0}".format(score))

    # each fram check if any aliens are touching the space ship
    for alien_number in range(len(aliens)):
      if aliens[alien_number].x > 0:
        if stage.collide(
            aliens[alien_number].x + 1,
            aliens[alien_number].y,
            aliens[alien_number].x + 15,
            aliens[alien_number].y + 15,
            ship.x,
            ship.y,
            ship.x + 15,
            ship.y + 15,
        ):
          # alien hit the ship
          sound.stop()
          sound.play(crash_sound)
          time.sleep(3.0)
          game_over_scene(score)
    # redraw Sprites
    game.render_sprites(lasers + [ship] + aliens)
    game.tick()  # wait until refresh rate finishes


def game_over_scene(final_score):
  # this function is the game over scene

  # image banks for CircuitPython
  image_bank_2 = stage.Bank.from_bmp16(IMAGE_BANK_MT_BACKGROUND_SETTING)

  # sets the background to image 0 in the image bank
  background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X,
                          constants.SCREEN_GRID_Y)

  # add text objects
  text = []
  text1 = stage.Text(width=29,
                     height=14,
                     font=None,
                     palette=constants.RED_PALETTE,
                     buffer=None)
  text1.move(22, 20)
  text1.text("Final Score: {:0>2d}".format(final_score))
  text.append(text1)

  text2 = stage.Text(width=29,
                     height=14,
                     font=None,
                     palette=constants.RED_PALETTE,
                     buffer=None)
  text2.move(43, 60)
  text2.text("GAME OVER")
  text.append(text2)

  text3 = stage.Text(width=29,
                     height=14,
                     font=None,
                     palette=constants.RED_PALETTE,
                     buffer=None)
  text3.move(32, 110)
  text3.text("PRESS SELECT")
  text.append(text3)

  # create a stage for the background to show up on
  #  and set the frame rate to 60fps
  game = stage.Stage(ugame.display, constants.FPS)
  # set the layers, items show up in order
  game.layers = text + [background]
  # render the background and intial location of sprite list
  # most likely you will only render background once per scene
  game.render_block()

  # repeat forever, game loop
  while True:
    # get user input
    keys = ugame.buttons.get_pressed()
    # Start button selected
    if keys & ugame.K_SELECT != 0:
      supervisor.reload()

    # update game logic
    game.tick()  # wait unitl refresh rate finishes


if __name__ == "__main__":
<<<<<<< HEAD
  splash_scene()
=======
    menu_scene()
>>>>>>> fa8497a8c1f4c58a15dcbcbf7cdaab58ab0b1930
