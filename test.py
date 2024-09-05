import pygame
import sys

class PlatformerGame:
    def __init__(self):
        # Initialize PyGame and set up the display
        pygame.init()
        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Platformer Game')
        
        # Define colors
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        
        # Define rectangle properties
        self.rect_width, self.rect_height = 50, 50
        self.rect_x, self.rect_y = self.width // 2, self.height // 2
        self.rect_speed = 5
        
        # Set up the clock for controlling the frame rate
        self.clock = pygame.time.Clock()
    
    def handle_events(self):
        # Handle user input and other events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        # Get the current state of the keyboard
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect_x -= self.rect_speed
        if keys[pygame.K_RIGHT]:
            self.rect_x += self.rect_speed
        if keys[pygame.K_UP]:
            self.rect_y -= self.rect_speed
        if keys[pygame.K_DOWN]:
            self.rect_y += self.rect_speed

    def draw(self):
        # Fill the screen with black and draw the rectangle
        self.screen.fill(self.black)
        pygame.draw.rect(self.screen, self.white, pygame.Rect(self.rect_x, self.rect_y, self.rect_width, self.rect_height))
        pygame.display.flip()
    
    def run(self):
        # Main game loop
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

# Create an instance of the game and run it
if __name__ == "__main__":
    game = PlatformerGame()
    game.run()
