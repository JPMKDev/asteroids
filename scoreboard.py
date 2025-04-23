import pygame

class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.score = 0
        self.font = pygame.font.Font(None, 32)
    
    def update(self, score_change):
        self.score += score_change

    def draw(self, screen):
        text = self.font.render(f"Score: {self.score}", True, "white", None)
        text_rect = text.get_rect()
        screen.blit(text, text_rect)