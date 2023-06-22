import pygame


class Scoreboard:
    """ """

    def __init__(
            self,
            ai_settings,
            screen,
    ):
        """ Initialize score-board attributes """
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Prepare the initial score images
        self.prep_score()
        self.prep_high_score()

    # ----------------------------------------------- Score --------------------------------------
    def prep_score(self):
        """ Turn the score to a rendered image """
        score_str = f"Score: {int(self.ai_settings.score):,}"
        self.score_img = self.ai_settings.game_font.render(
            score_str,
            True,
            self.ai_settings.dark
        )

        # Display the score at the top-left of the screen
        self.score_rect = self.score_img.get_rect()
        self.score_rect.left = self.screen_rect.left + 10
        self.score_rect.top = self.screen_rect.top + 5

    # ----------------------------------------- HighScore ------------------------------------------
    def prep_high_score(self):
        """ Turn the high score into a rendered image. """
        high_score_str = "High Score: {:,}".format(int(self.ai_settings.high_score))

        self.high_score_image = self.ai_settings.game_font.render(
            high_score_str,
            True,
            self.ai_settings.dark
        )

        # Display the score at the top-left of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.top = self.score_rect.top
        self.high_score_rect.left = self.screen_rect.left + 600

    def show_states(self):
        """ Draw score to the screen"""
        # Message
        self.screen.blit(
            self.msg,
            (200, 200)
        )

    def show_high_score(self):
        # High score
        self.screen.blit(
            self.high_score_image,
            self.high_score_rect
        )

    def show_score(self):
        # Score
        self.screen.blit(
            self.score_img,
            self.score_rect
        )
