import pygame

image_size = 64

jay_sprite = pygame.image.load("assets/ninjas/JAY2.png")
jay_list = [
    jay_sprite.subsurface(pygame.Rect(i * image_size, 0, image_size, image_size))
    for i in range(6)
]

class Player:
    def __init__(self):
        self.image_index = 0
        self.frame = jay_list[self.image_index]
        self.rect = pygame.Rect(0, 0, image_size, image_size)
        self.frame_timer = 0
    
    def reset_pos(self):
        self.rect.x = 500
        self.rect.y = 336
    
    def update(self, dt:int):
        self.frame_timer += dt

        if self.frame_timer >= 100:
            self.image_index = (self.image_index + 1)%6
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.rect.y += 5
            self.frame = jay_list[self.image_index]
        elif keys[pygame.K_UP]:
            self.rect.y -= 5
        elif keys[pygame.K_LEFT]:
            self.rect.x -= 5
        elif keys[pygame.K_RIGHT]:
            self.rect.x += 5
    
    def draw(self, surface:pygame.Surface):
        surface.blit(self.frame, (self.rect.x, self.rect.y))
        pygame.draw.rect(surface, (255, 0, 0), self.rect, 1)