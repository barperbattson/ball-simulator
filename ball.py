import pygame as pg

class Ball(pg.sprite.Sprite):
    def __init__(self, window, radius, color, initPos, initVel, gravity, elasticity, friction):
        super().__init__()
        
        # WINDOW ATTRIBUTES
        self.window = window
        self._WIDTH = window.get_width()
        self._HEIGHT = window.get_height()
        
        # BALL PROPERTIES
        self.radius = radius
        self.image = pg.Surface((2*radius, 2*radius), pg.SRCALPHA)
        self.color = color

        pg.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)

        self.rect = self.image.get_rect(center=initPos)

        # VELOCITY VARIABLES
        self.velX = initVel[0]
        self.velY = initVel[1]

        # MOVEMENT VARIABLES
        self.gravity = gravity
        self.elasticity = elasticity
        self.friction = friction

    def update(self, width, height):
        # APPLY GRAVITY
        self.velY += self.gravity

        # UPDATE POSITION
        self.rect.x += self.velX
        self.rect.y += self.velY

        # CHECK FOR COLLISIONS WITH THE FLOOR
        if self.rect.bottom >= self._HEIGHT:
            self.rect.bottom = self._HEIGHT # RESET POSITION TO THE SURFACE OF THE FLOOR
            self.velY = -self.velY * self.elasticity # REVERSE AND REDUCE VERTICAL VELOCITY

            # APPLY FRICITON WHEN BOUNCING ON THE FLOOR
            self.velX *= self.friction

        # CHECK FOR COLLISIONS WITH THE CEILING
        if self.rect.top <= 0:
            self.rect.top = 0
            self.velY = -self.velY * self.elasticity

        # CHECK FOR COLLISIONS WITH THE WALLS
        if self.rect.right >= self._WIDTH:
            self.rect.right = self._WIDTH
            self.velX = -self.velX * self.elasticity
        elif self.rect.left <= 0:
            self.rect.left = 0
            self.velX = -self.velX * self.elasticity
        