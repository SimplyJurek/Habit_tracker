# imports
import pygame
import Global as GLOBAL
from Button import Button

# --- --- ---

class Main:
    '''Main Program Class'''
    def __init__(self):
        '''Main Program Class Constructor'''
        pygame.init()

        self.screen = GLOBAL.SCREEN
        self.clock = GLOBAL.CLOCK
        
        self.run()

    def run(self):
        '''Main Program Run Function'''
        self.screen.fill(GLOBAL.BG_COLOR)
        terminated = False
        # Main menu buttons config
        font_size = 40
        size = (300, 150)

        buttons = []
        track_habits_button = Button(
            text='Track Habits', 
            font_size=font_size, 
            position=(GLOBAL.SCREEN_SIZE[0] / 2 - 150, GLOBAL.SCREEN_SIZE[1] / 2 - 240), 
            size=size
            )
        buttons.append(track_habits_button)

        add_habits_button = Button(
            text='Add Habits', 
            font_size=font_size, 
            position=(GLOBAL.SCREEN_SIZE[0] / 2 - 150, GLOBAL.SCREEN_SIZE[1] / 2 - 75), 
            size=size
            )
        buttons.append(add_habits_button)

        view_progress_button = Button(
            text='View Progress', 
            font_size=font_size, 
            position=(GLOBAL.SCREEN_SIZE[0] / 2 - 150, GLOBAL.SCREEN_SIZE[1] / 2 + 90), 
            size=size
            )
        buttons.append(view_progress_button)


        while not terminated:
            mouse_position = pygame.mouse.get_pos()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                

            for button in buttons:
                button.check_collision(mouse_position)
                button.draw()

            pygame.display.flip()
            self.clock.tick(GLOBAL.FPS)


if __name__ == '__main__':
    Main()