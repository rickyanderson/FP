import pygame
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.move = True
        self.image = pygame.Surface((20,20),pygame.SRCALPHA)
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.edge = False
        self.stop = False
        self.rect.x, self.rect.y = (x, y)
        self.currentspeed = 10
        self.timer = 0
    def update(self):
        if not self.stop:
            self.timer += self.currentspeed
            if not self.edge:
                if self.rect.x == 0 and self.timer > 50:
                    self.rect.x = 21
                    self.timer = 0
                if self.rect.x == 21 and self.timer > 50:
                    self.rect.x = 42
                    self.timer = 0
                if self.rect.x == 42 and self.timer > 50:
                    self.rect.x = 63
                    self.timer = 0
                if self.rect.x == 63 and self.timer > 50:
                    self.rect.x = 84
                    self.timer = 0
                if self.rect.x == 84 and self.timer > 50:
                    self.rect.x = 105
                    self.timer = 0
                if self.rect.x == 105 and self.timer > 50:
                    self.rect.x = 126
                    self.timer = 0
                if self.rect.x == 126 and self.timer > 50:
                    self.rect.x = 147
                    self.timer = 0
                if self.rect.x == 147 and self.timer > 50:
                    self.rect.x = 168
                    self.timer = 0
                if self.rect.x == 168 and self.timer > 50:
                    self.rect.x = 189
                    self.timer = 0
                if self.rect.x == 189 and self.timer > 50:
                    self.rect.x = 210
                    self.timer = 0
                if self.rect.x == 210 and self.timer > 50:
                    self.rect.x = 231
                    self.timer = 0
                if self.rect.x == 231 and self.timer > 50:
                    self.rect.x = 252
                    self.timer = 0
            else:
                if self.rect.x == 21 and self.timer > 50:
                    self.rect.x = 0
                    self.timer = 0
                if self.rect.x == 42 and self.timer > 50:
                    self.rect.x = 21
                    self.timer = 0
                if self.rect.x == 63 and self.timer > 50:
                    self.rect.x = 42
                    self.timer = 0
                if self.rect.x == 84 and self.timer > 50:
                    self.rect.x = 63
                    self.timer = 0
                if self.rect.x == 105 and self.timer > 50:
                    self.rect.x = 84
                    self.timer = 0
                if self.rect.x == 126 and self.timer > 50:
                    self.rect.x = 105
                    self.timer = 0
                if self.rect.x == 147 and self.timer > 50:
                    self.rect.x = 126
                    self.timer = 0
                if self.rect.x == 168 and self.timer > 50:
                    self.rect.x = 147
                    self.timer = 0
                if self.rect.x == 189 and self.timer > 50:
                    self.rect.x = 168
                    self.timer = 0
                if self.rect.x == 210 and self.timer > 50:
                    self.rect.x = 189
                    self.timer = 0
                if self.rect.x == 231 and self.timer > 50:
                    self.rect.x = 210
                    self.timer = 0
                if self.rect.x == 252 and self.timer > 50:
                    self.rect.x = 231
                    self.timer = 0
        if self.stop:
            None
