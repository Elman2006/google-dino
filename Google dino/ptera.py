class Ptera:
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

        # # Load the bird image and get its rect
        # self.ptera_image = ai_settings.dino_img
        # self.ptera_rect = self.ptera_image.get_rect()

        # # Set the position of the ptera
        # self.ptera_rect.top = 330
        # self.ptera_rect.left = self.screen_rect.right

    def generate_ptera(self):
        ptera_rect = self.ai_settings.ptera_img.get_rect(midtop=(self.screen_rect.right, self.ai_settings.ptera_y))
        return ptera_rect

    def blit_ptera(self):
        """ Show the dino in the screen """
        for _ptera_ in self.ai_settings.ptera_list_img:
            self.screen.blit(
                self.ai_settings.ptera_img,
                _ptera_
            )
