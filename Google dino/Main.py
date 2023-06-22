# ========================================== Modules =============================================
# ------------------------------------ Open modules --------------------------------------------
import pygame

# ------------------------------------ My modules -----------------------
from settings import Settings
import functions as gf
from dino import Dino
from cacti import Cacti
from score_bord import Scoreboard
from ptera import Ptera


# ========================================== Infinity loop ============================================
def run_game():
    # initialize
    pygame.init()

    # Create objects
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,
         ai_settings.screen_height)
    )
    cacti = Cacti(ai_settings, screen)
    dino = Dino(ai_settings, screen)
    ptera = Ptera(ai_settings, screen)
    sb = Scoreboard(ai_settings, screen)
    clock = pygame.time.Clock()

    while True:
        """ An infinity loop for updating the screen"""

        # Set the FPS
        clock.tick(ai_settings.fps)

        # To get all events in game
        gf.check_events(ai_settings, cacti, dino, ptera)

        # When the game not start yet
        if not ai_settings.game_active:
            screen.blit(ai_settings.screen_bg, (0, 0))
            screen.blit(ai_settings.dino_stop, (25, 330))
            screen.blit(ai_settings.start_background, (100, 50))

        # When the game starts
        if ai_settings.game_active:

            # Background movement
            gf.move_bg(
                ai_settings, screen)

            # Check for the collision between dino and cactus & ptera
            gf.check_collision(ai_settings, dino)

            # Move and blit the dino, ptera and cactus
            # Dino
            gf.dino_movement(ai_settings, dino)

            # ptera
            gf.ptera_movement(ai_settings, ptera)

            # Cacti
            ai_settings.cacti_list = gf.cacti_movement(ai_settings)
            cacti.blit_cacti()

            # To update and increase the score
            gf.update_score(ai_settings, sb)

        gf.update_screen(ai_settings, sb)


# ======================================== Call the start function =========================================
run_game()
