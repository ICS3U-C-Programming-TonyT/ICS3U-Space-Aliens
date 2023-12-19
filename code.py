#!/usr/bin/env python3
# Created By: Tony Tran
# Date: December. 11, 2023
# This program is the "Space Aliens" program on the PyBadge

import stage
import ugame
import constants

def menu_scene_2():
    # this function is the menu scene

    # image banks for CircuitPython
    image_bank_mt_background = stage.Bank.from_bmp16("images\mt_game_studio.bmp")
    
    # Settings
    select = "start"

    # add text objects
    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("Capybara Catcher")
    text.append(text1)

    start_text = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    start_text.move(40, 60)
    start_text.text("> START <")
    text.append(start_text)

    instruction_text = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    instruction_text.move(40, 90)
    instruction_text.text("INSTRUCTIONS")
    text.append(instruction_text)

    # sets the background to image 0 in the image bank
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_X, constants.SCREEN_Y)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers, items show up in order
    game.layers = text + [background]
    # render the background and initial location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    while True:
        # settings options
        options = {
            1:"start",
            2:"instructions",
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
        game.tick()

def menu_scene_1():
    # this function is the menu scene

    # image banks for CircuitPython
    image_bank_mt_background = stage.Bank.from_bmp16("images\mt_game_studio.bmp")
    
    # Settings
    select = "start"

    # add text objects
    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("Capybara Catcher")
    text.append(text1)

    start_text = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    start_text.move(40, 60)
    start_text.text("> START <")
    text.append(start_text)

    instruction_text = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    instruction_text.move(40, 90)
    instruction_text.text("INSTRUCTIONS")
    text.append(instruction_text)

    # sets the background to image 0 in the image bank
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_X, constants.SCREEN_Y)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers, items show up in order
    game.layers = text + [background]
    # render the background and initial location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    while True:
        # settings options
        options = {
            1:"start",
            2:"instructions",
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
        game.tick()

def game_scene():
    # this function is the main game game_scene

    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("images\space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("images\sprites\space_aliens.bmp")
    
    # buttons that you want to keep state information on

    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # get sound ready
    pew_sound = open("audio\pew.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # set the background to image 0 in the image bank
    #   and the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # a sprite that will be updated every frame
    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2*constants.SPRITE_SIZE))

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers of all sprites, items show up in order
    game.layers = [ship] + [background]
    # render all sprites
    #   most likely you will only render the background once per game scene
    game.render_block()

    # repeat forever, game loop
    while True:

        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_X != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
            else:
                if a_button == constants.button_state["button_still_pressed"]:
                    a_button = constants.button_state["button_released"]
                else:
                    a_button = constants.button_state["button_up"]
        if keys & ugame.K_O != 0:
            pass
        if keys & ugame.K_START != 0:
            pass
        if keys & ugame.K_SELECT != 0:
            pass
        if keys & ugame.K_RIGHT != 0:
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)
            else:
                pass
        if keys & ugame.K_LEFT != 0:
            if ship.x >= 0:
                ship.move(ship.x - 1, ship.y)
            else:
                pass
        if keys & ugame.K_UP != 0:
            pass
        if keys & ugame.K_DOWN != 0:
            pass
        
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)

        game.render_sprites([ship])
        game.tick()

if __name__ == "__main__":
    menu_scene_1()
