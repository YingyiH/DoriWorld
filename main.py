import pygame
from breakout.screens import WelcomeScreen,PrepareScreen,GameScreen,GameOverScreen,MenuScoreScreen


class Game:
    """Main class for the application"""

    def __init__(self):
        # Creates the window
        self.window = pygame.display.set_mode((1050, 550))
        pygame.display.set_caption('DoriWorld')

    def run(self):
        # Available screens:
        screens = {
            "welcome": WelcomeScreen,
            "menuscore": MenuScoreScreen,
            "prepare": PrepareScreen,
            "game": GameScreen,
            "gameover": GameOverScreen
        }
        scores = {}

        # Start the loop
        running = True
        current_screen = "welcome"
        while running:
            # Obtain the screen class
            screen_class = screens.get(current_screen)
            if not screen_class:
                raise RuntimeError(f"Screen {current_screen} not found!")

            # Create a new screen object, "connected" to the window
            screen = screen_class(self.window,scores)

            # Run the screen
            screen.run()

            # When the `run` method stops, we should have a `next_screen` setup
            if screen.next_screen is False:
                running = False
            # Switch to the next screen
            current_screen = screen.next_screen


if __name__ == "__main__":
    doriWorld = Game()
    doriWorld.run()
