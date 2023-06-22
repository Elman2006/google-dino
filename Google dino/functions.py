# ======================================== Modules ==================================================
# ---------------------------------------- Open Modules --------------------------------------------
import pygame
from sys import exit
from random import randrange


# ======================== Events ======================
def check_down(
        ai_settings,
        dino,
        event):
    """ Respond when the player press's the key"""

    # Exit the game
    if event.key == pygame.K_ESCAPE:
        exit()

    # Start game
    elif event.key == pygame.K_SPACE and not ai_settings.game_active:
        pygame.mouse.set_visible(False)
        ai_settings.game_active = True

    # Jump dino
    if event.key == pygame.K_SPACE and ai_settings.game_active and dino.dino_rect.top == 330:
        ai_settings.jump_sound.play()
        ai_settings.dino_jump = 0
        ai_settings.dino_jump += ai_settings.jump

    # Make the dino duking run
    if event.key == pygame.K_DOWN:
        ai_settings.dino_ducking = True


def check_up(
        ai_settings,
        event
):
    """ Respond when the player press's the key"""
    if event.key == pygame.K_DOWN:
        ai_settings.dino_ducking = False


def check_events(
        ai_settings,
        cacti,
        dino,
        ptera
):
    """ Check for all events in game """

    for event in pygame.event.get():

        # Exit from the game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Check for key presses
        elif event.type == pygame.KEYDOWN:
            check_down(
                ai_settings,
                dino,
                event
            )

        # Check for key ups
        elif event.type == pygame.KEYUP:
            check_up(
                ai_settings,
                event
            )

        # Creat animation of running dino
        elif event.type == ai_settings.create_run and not ai_settings.dino_ducking and ai_settings.game_active:
            dino.dino_image = dino_animation(ai_settings)
            if ai_settings.dino_list_index == 0:
                ai_settings.dino_list_index += 1
            elif ai_settings.dino_list_index == 1:
                ai_settings.dino_list_index -= 1

        # Creat animation of running dino ducking
        elif event.type == ai_settings.create_run and ai_settings.game_active and ai_settings.dino_ducking:
            dino.dino_image = dino_ducking(ai_settings)
            if ai_settings.dino_list_index == 0:
                ai_settings.dino_list_index += 1
            elif ai_settings.dino_list_index == 1:
                ai_settings.dino_list_index -= 1

        # Creat cactus
        elif event.type == ai_settings.create_cacti and ai_settings.game_active:
            cacti.cacti_img()
            ai_settings.cacti_list.append(cacti.generate_cacti())

        # Creat fly animation
        elif event.type == ai_settings.create_fly:
            if ai_settings.ptera_list_index == 0:
                ai_settings.ptera_list_index += 1
            elif ai_settings.ptera_list_index == 1:
                ai_settings.ptera_list_index -= 1
            ptera.ptera_image = ptera_animation(ai_settings)


# ======================================== Move ground =========================================
def move_bg(
        ai_settings,
        screen
):
    """ Make the background that can move"""
    # Blit the background
    screen.blit(ai_settings.screen_bg, (ai_settings.bg_img_x, 0))
    screen.blit(ai_settings.screen_bg, (ai_settings.bg_img_x + 1203, 0))

    # Move the backgrounds to left
    ai_settings.bg_img_x -= ai_settings.ground_speed_factor

    # reset the movement
    if ai_settings.bg_img_x <= -1203:
        ai_settings.bg_img_x = 0


# ======================================== control dino =========================================
def dino_movement(
        ai_settings,
        dino
):
    """ A function to control dino"""
    # Blit the dino
    dino.blit_dino()

    # Move the dino
    dino.dino_rect.centery += ai_settings.dino_jump
    if dino.dino_rect.top < 330:

        # If dino's height is less than 330 we increase to gravity to pull it down
        ai_settings.dino_jump += ai_settings.gravity

    elif ai_settings.dino_ducking:
        dino.dino_rect.top = 370

    else:
        dino.dino_rect.top = 330


def dino_ducking(ai_settings):
    """ Change the image type """
    ai_settings.dino_img = ai_settings.dino_list_duking[ai_settings.dino_list_index]
    return ai_settings.dino_img


def dino_animation(ai_settings):
    """ To make an animation of run  in google dino"""
    ai_settings.dino_img = ai_settings.dino_list[ai_settings.dino_list_index]
    return ai_settings.dino_img


# ======================================== control ptera =========================================
def ptera_animation(ai_settings):
    """ To make the animation of flying ptera in game"""
    ai_settings.ptera_img = ai_settings.ptera_list[ai_settings.ptera_list_index]
    return ai_settings.ptera_img


def ptera_height(ai_settings):
    """ To make a random height to the ptera between 140 and 340"""
    ai_settings.ptera_y = randrange(200, 340, 15)


def creat_ptera(ai_settings, ptera):
    """ Creating the petras and add them to a list """
    for _cacti_ in ai_settings.cacti_list:
        if 400 < _cacti_.centerx < 405:
            ai_settings.ptera_list_img.append(ptera.generate_ptera())


def ptera_movement(
        ai_settings,
        ptera
):
    """ A function to creat and move cacti"""
    # Display the ptera on the screen
    ptera.blit_ptera()
    ptera_height(ai_settings)
    creat_ptera(ai_settings, ptera)

    # Move the pteras that in the list
    for _ptera_ in ai_settings.ptera_list_img:
        _ptera_.centerx -= ai_settings.ground_speed_factor

    # Remove the ptera that are out of screen
    inside_pteras = [_ptera_ for _ptera_ in ai_settings.ptera_list_img if _ptera_.right > 0]
    return inside_pteras


# ========================= creat and move cacti ======================
def cacti_movement(
        ai_settings
):
    """ A function to creat and move cacti"""
    for _cacti_ in ai_settings.cacti_list:
        _cacti_.centerx -= ai_settings.ground_speed_factor

    # Remove the cacti that are out of screen
    inside_cactis = [_cacti_ for _cacti_ in ai_settings.cacti_list if _cacti_.right > 0]
    return inside_cactis


# ========================= collision ======================
def restart(ai_settings,
            dino):
    """ To restart the game """
    pygame.mouse.set_visible(True)
    ai_settings.cacti_list.clear()
    ai_settings.ptera_list_img.clear()
    ai_settings.score = 0
    dino.dino_rect.top = 330


def game_over(ai_settings, dino):
    """ The actions when dino collied with cacti or ptera"""

    # TODO: I want to blit the dino die image before playing new round
    dino.dino_image = ai_settings.dino_die

    ai_settings.die_sound.play()
    pygame.time.wait(2000)
    ai_settings.game_active = False


def check_collision(
        ai_settings,
        dino):
    """ Check the collision between dino and petra or cacti"""
    for cacti in ai_settings.cacti_list:
        if dino.dino_rect.colliderect(cacti):
            game_over(ai_settings, dino)
            restart(ai_settings, dino)

    for ptera in ai_settings.ptera_list_img:
        if dino.dino_rect.colliderect(ptera):
            game_over(ai_settings, dino)
            restart(ai_settings, dino)


# ========================================= Update the screen and score ===============================================
def update_score(ai_settings,
                 sb):
    """ to control and increase the score"""
    for _cacti_ in ai_settings.cacti_list:
        if 42 < _cacti_.right < 50:
            ai_settings.score += ai_settings.score_point

        elif ai_settings.score >= ai_settings.high_score:
            ai_settings.high_score = ai_settings.score

    # Show the score and high score in the bord
    sb.prep_high_score()
    sb.prep_score()


def update_screen(
        ai_settings,
        sb
):
    """ To make the most recent screen """
    # Screen
    pygame.display.set_caption(ai_settings.caption)
    pygame.display.set_icon(ai_settings.icon)

    # Score
    sb.show_score()
    sb.show_high_score()

    pygame.display.flip()
