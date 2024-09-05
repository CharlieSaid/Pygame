import pygame
import sys

class Game:
    def __init__(self):

        pygame.init() # Start Pygame

        pygame.display.set_caption('Dungeon_Game') # Title
        self.screen = pygame.display.set_mode((800,600)) # Set up the screen dimensions

        self.clock = pygame.time.Clock() # Initialize the clock

        self.p_pos = [50,200]
        self.p_base_speed = 5

        # Jump mechanics
        self.p_jump = False
        self.p_jump_vel = 0

        self.gravity = .5  # Gravity constant
        self.jump_strength = -10 # Jump strength
        self.ground = 300 # Ground level (TEMPORARY)

        self.p_img = pygame.image.load('my_images/d 2/sprite_0 Background Removed.png').convert()
        self.p_img.set_colorkey((0,0,0))

    def update(self):
        # Get the current state of the keyboard
        keys = pygame.key.get_pressed()

        # Process user input
        if keys[pygame.K_d]:
            self.p_pos[0] += self.p_base_speed
        if keys[pygame.K_a]:
            self.p_pos[0] -= self.p_base_speed
        if keys[pygame.K_SPACE] and not self.p_jump:
            self.p_jump = True
            self.p_jump_vel = self.jump_strength
            print('jumping!')

        # Handle jumping status
        if self.p_jump:
            self.p_jump_vel += self.gravity
            self.p_pos[1] += self.p_jump_vel

            if self.p_pos[1] >= self.ground:
                self.p_pos[1] = self.ground
                self.p_jump = False
                self.p_jump_vel = 0
                print('landed!')

    def run(self):

        while True:
            self.screen.fill((100,100,255))

            self.screen.blit(self.p_img,self.p_pos)

            # Quit button on window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.update()

            pygame.display.flip() # Update the screen each tick.  .update() = update objects within an area, .flip() = update the whole screen.
            self.clock.tick(60) # Establish the fps.

Game().run()