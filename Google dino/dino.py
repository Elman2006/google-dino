class Dino:
    """ A class to manage and control dino"""

    def __init__(
            self,
            ai_settings,
            screen
    ):
        """ Initialize bird attributes"""

        # Objects
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        # Load the bird image and get its rect
        self.dino_image = ai_settings.dino_img
        self.dino_rect = self.dino_image.get_rect()

        # Set the position of the dino
        self.dino_rect.top = 330
        self.dino_rect.left = 25

    def blit_dino(self):
        """ Show the dino in the screen """
        self.screen.blit(
            self.dino_image,
            self.dino_rect
        )
