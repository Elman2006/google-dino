from random import randint


class Cacti:
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

    def cacti_img(self):
        """ To make different cactis"""
        self.ai_settings.cacti_img_list = [
            self.ai_settings.cacti_21,
            self.ai_settings.cacti_22,
            # self.ai_settings.cacti_5,
            # self.ai_settings.cacti_4
        ]
        rand = randint(0, 1)
        self.ai_settings.cacti_img = self.ai_settings.cacti_img_list[rand]

    def generate_cacti(self):
        cacti_rect = self.ai_settings.cacti_img.get_rect(midbottom=(self.screen_rect.right, 430))
        return cacti_rect

    def blit_cacti(self):
        """ Show the dino in the screen """
        for _cacti_ in self.ai_settings.cacti_list:
            self.screen.blit(
                self.ai_settings.cacti_img,
                _cacti_
            )
