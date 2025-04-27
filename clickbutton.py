from asset import Asset

import subprocess
import sys
import pygame

class ClickButton(Asset):
    def __init__(self, button_image, button_name):
            super().__init__(button_image, 650, 300, 0.6)
            self.name = button_name
    
    def clicked(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if self.name == "play":
                print("Starting level 1")
                subprocess.Popen(["python3", "level1.py"])
                sys.exit()
            elif self.name == "levels":
                subprocess.Popen(["python3", "level_selector.py"])
                sys.exit()