import pygame

def load_image(file_path):
    try:
        image = pygame.image.load(file_path).convert()
        return image
    except pygame.error as e:
        print(f"Unable to load image: {file_path}")
        raise SystemExit(e)

