import pygame
import sys

class Ship:
    """ship image and its properties"""
    def __init__(self,ai_game):
        """places the ship at the bottom of screen"""
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()
        #load the ship
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.rect.midbottom=self.screen_rect.midbottom

    def blitme(self):
        """displays the ship at its location"""
        self.screen.blit(self.image,self.rect)

