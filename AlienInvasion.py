import pygame
import sys
from settings import Settings
from rocketship import Ship

class AlienInvasion:
    """A class to manage the game"""
    def __init__(self):
        pygame.init()
        self.settings=Settings()
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_length))
        self.ship=Ship(self)
    def run_game(self):
        while True:
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                self.screen.fill(self.settings.bgcolor)
                self.ship.blitme()
                pygame.display.flip()

if __name__=='__main__':
    ai=AlienInvasion()
    ai.run_game()