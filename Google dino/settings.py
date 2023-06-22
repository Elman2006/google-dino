import pygame


class Settings:
    """ A class to manage game settings"""

    def __init__(self):
        """ Initialize game's static settings"""

        # ********************** Color **********************
        self.background_col = (235, 235, 235)

        # ********************** Files **********************
        self.icon = pygame.image.load("sprites/dino/chrom_dino.jpg")
        self.screen_bg = pygame.image.load("sprites/background/screen_bg_colored.jpg")
        self.jump_sound = pygame.mixer.Sound("sprites/Sounds/jump.wav")
        self.die_sound = pygame.mixer.Sound("sprites/Sounds/die.wav")
        self.game_font = pygame.font.Font("sprites/Font/Flappy.TTF", 36)

        # Dino
        self.dino_run1 = pygame.image.load("sprites/Dino/dino-run1.png")
        self.dino_run2 = pygame.image.load("sprites/Dino/dino-run2.png")
        self.dino_die = pygame.image.load("sprites/Dino/dino-die.png")
        self.dino_stop = pygame.image.load("sprites/Dino/dino-stop.png")
        self.dino_ducking1 = pygame.image.load("sprites/Dino/dino_ducking1.png")
        self.dino_ducking2 = pygame.image.load("sprites/Dino/dino_ducking2.png")
        self.start_background = pygame.image.load("sprites/Background/Untitled-1.png")

        # Ptera
        self.ptera_up = pygame.image.load("sprites/Ptera/ptera.png")
        self.ptera_down = pygame.image.load("sprites/Ptera/ptera copy.png")

        # Cacti
        self.cacti_21 = pygame.image.load("sprites/cacti/cacti-big-2.png")
        self.cacti_22 = pygame.image.load("sprites/cacti/cacti-big.png")
        self.cacti_4 = pygame.image.load("sprites/cacti/cacti-big-4.png")
        self.cacti_5 = pygame.image.load("sprites/cacti/cacti-big-5.png")

        # ********************** Screen settings **********************
        self.screen_width = 1038
        self.screen_height = 474
        self.fps = 60
        self.caption = "Google dino"

        # Colors
        self.dark = (30, 40, 60)

        # ********************** Ground **********************
        self.bg_img_x = 0
        self.ground_speed_factor = 6

        # ********************** Dino **********************
        self.dino_list = [
            self.dino_run1,
            self.dino_run2,
            self.dino_die
        ]
        self.dino_list_duking = [
            self.dino_ducking1,
            self.dino_ducking2
        ]
        self.cacti_list = []
        self.cacti_img = ""
        self.dino_list_index = 0
        self.dino_img = self.dino_list[self.dino_list_index]
        self.dino_jump = 0
        self.time_to_blit = pygame.time.get_ticks() + 2000
        self.dino_ducking = False
        self.jump = -14
        self.gravity = 0.5

        # ********************** Ptera **********************
        self.ptera_list = [
            self.ptera_up,
            self.ptera_down
        ]
        self.ptera_list_index = 0
        self.ptera_img = self.ptera_list[self.ptera_list_index]
        self.ptera_list_img = []
        self.ptera_y = 340

        # ********************** States **********************
        self.game_active = False
        self.score = 0
        self.high_score = 0
        self.score_point = 2

        # ************************ User events ***************************
        # To make dino animation
        self.create_run = pygame.USEREVENT
        pygame.time.set_timer(self.create_run, 400)

        # To make fly animation
        self.create_fly = pygame.USEREVENT + 1
        pygame.time.set_timer(self.create_fly, 200)

        # The period of creating the cacti
        self.create_cacti = pygame.USEREVENT + 2
        pygame.time.set_timer(self.create_cacti, 3000)

        # The period of creating the ptera
        self.create_ptera = pygame.USEREVENT + 3
        pygame.time.set_timer(self.create_ptera, 2000)
