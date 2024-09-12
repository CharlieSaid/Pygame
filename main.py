
# git add .
# git commit -m "your commit message"
# git push origin master





import pygame
import sys

from graphics_utils import load_image

class Game:
    def __init__(self):

        pygame.init() # Start Pygame

        pygame.display.set_caption('Dungeon_Game') # Title

        self.scale_factor = 2
        self.screen_dimensions = (800,600)
        self.screen = pygame.display.set_mode(self.screen_dimensions) # Set up the screen dimensions
        self.display = pygame.Surface((self.screen_dimensions[0]//self.scale_factor,self.screen_dimensions[1]//self.scale_factor))

        self.clock = pygame.time.Clock() # Initialize the clock

        self.p_pos = [50,200]
        self.p_base_speed = 5/self.scale_factor
        self.movement = [False,False] # Moving left, Moving right
        self.move_counter = 0
        self.p_img_index = 0

        # Jump mechanics
        self.p_jump = False
        self.p_jump_vel = 0

        self.gravity = .5  # Gravity constant
        self.jump_strength = -10 # Jump strength
        self.ground = 300/self.scale_factor # Ground level (TEMPORARY)

        self.p_imgs = [load_image('my_images/player/sprite_1.png'),load_image('my_images/player/sprite_2.png')]
        #for img in self.p_imgs: img.set_colorkey((0,0,0))
        self.p_imgs = [load_image('my_images/player/sprite_1.png')]

    def update(self):
        self.movement = [False,False]
        # Get the current state of the keyboard
        keys = pygame.key.get_pressed()

        # Process user input
        if keys[pygame.K_d]:
            self.movement[0] = True
            #self.p_pos[0] += self.p_base_speed
        if keys[pygame.K_a]:
            self.movement[1] = True
            #self.p_pos[0] -= self.p_base_speed
        if keys[pygame.K_SPACE] and not self.p_jump:
            self.p_jump = True
            self.p_jump_vel = self.jump_strength
            print('jumping!')

        # Handle movement
        if self.movement[0]:
            self.p_pos[0] += self.p_base_speed
            self.move_counter += 1
        if self.movement[1]:
            self.p_pos[0] -= self.p_base_speed
            self.move_counter += 1

        # Handle jumping status
        if self.p_jump:
            self.p_jump_vel += self.gravity
            self.p_pos[1] += self.p_jump_vel

            if self.p_pos[1] >= self.ground:
                self.p_pos[1] = self.ground
                self.p_jump = False
                self.p_jump_vel = 0
                print('landed!')

        # Handle animation
        if self.move_counter >=10:
            self.p_img_index = (self.p_img_index+1)%len(self.p_imgs)
            self.move_counter = 0

    def run(self):

        while True:
            self.display.fill((255,255,255)) # Color the display

            self.display.blit(self.p_imgs[self.p_img_index],self.p_pos) # Put the player on the display

            self.screen.blit(pygame.transform.scale(self.display,self.screen.get_size()),(0,0))

            # Quit button on window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.update()

            pygame.display.flip() # Update the screen each tick.  .update() = update objects within an area, .flip() = update the whole screen.
            self.clock.tick(60) # Establish the fps.

Game().run()