import pygame

def load_image(file_path):
    try:
        image = pygame.image.load(file_path)
        image.set_colorkey((0,0,0))
        image.convert() 
        # Convert changes the colors somehow which breaks the set_colorkey command.  
        # So we need to convert after we set color key.
        return image
    except pygame.error as e:
        print(f"Unable to load image: {file_path}")
        raise SystemExit(e)

def player_animate(fps):
    return fps