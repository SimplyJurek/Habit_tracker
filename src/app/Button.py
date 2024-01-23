# imports
import pygame
import Global as GLOBAL

# --- --- --- 

class Button:
    def __init__(
            self, 
            text, 
            font_size, 
            position, 
            size, 
            ):
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])
        self.text = text
        self.rect_fill = 0
        self.border_radius = 0
        self.border_top_left_radius = 0
        self.border_top_right_radius = 20
        self.border_bottom_left_radius = 20
        self.border_bottom_right_radius = 0
        self.font = pygame.font.SysFont('Cascadia Code ExtraLight', font_size)
        self.hover = False

    def draw(self):
        if self.hover:
            pygame.draw.rect(GLOBAL.SCREEN, 
                             GLOBAL.BUTTON_COLOR_HOVER, 
                             self.rect, self.rect_fill, 
                             self.border_radius, 
                             self.border_top_left_radius, 
                             self.border_top_right_radius, 
                             self.border_bottom_left_radius, 
                             self.border_bottom_right_radius
                             )
            text_surface = self.font.render(self.text, True, GLOBAL.TEXT_COLOR_HOVER)
        else:
            pygame.draw.rect(GLOBAL.SCREEN, 
                             GLOBAL.BUTTON_COLOR, 
                             self.rect, self.rect_fill, 
                             self.border_radius, 
                             self.border_top_left_radius, 
                             self.border_top_right_radius, 
                             self.border_bottom_left_radius, 
                             self.border_bottom_right_radius
                             )
            text_surface = self.font.render(self.text, True, GLOBAL.TEXT_COLOR)
        
        text_rect = text_surface.get_rect(center=self.rect.center)
        GLOBAL.SCREEN.blit(text_surface, text_rect)

    def check_collision(self, position):
        if self.rect.collidepoint(position):
            self.hover = True
        else: self.hover = False
        return self.rect.collidepoint(position)