import pygame

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

class Slider:

    def __init__(self, x, y, w, h, min_val, max_val, initial_val):
        self.rect = pygame.Rect(x, y, w, h)
        self.min_val = min_val
        self.max_val = max_val
        self.value = initial_val
        self.grabbed = False

    def draw(self, screen):
        # Draw the background
        pygame.draw.rect(screen, GRAY, self.rect)
        # Draw the handle (circle)
        handle_x = self.rect.x + (self.value - self.min_val) / (self.max_val - self.min_val) * self.rect.width
        pygame.draw.circle(screen, RED, (int(handle_x), self.rect.centery), self.rect.height // 2)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.grabbed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.grabbed = False
        elif event.type == pygame.MOUSEMOTION:
            if self.grabbed:
                mouse_x = event.pos[0]
                # Constrain the handle within the slider
                new_value = (mouse_x - self.rect.x) / self.rect.width * (self.max_val - self.min_val) + self.min_val
                self.value = max(self.min_val, min(self.max_val, new_value))
