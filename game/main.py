import pygame
import random as rand

# https://nerdparadise.com/programming

pygame.init()
fps = 60
spawnPadding = 40
screenX = 500
screenY = 400
screen = pygame.display.set_mode((screenX, screenY))
clock = pygame.time.Clock()
done = False

players = list()


class player():
    def __init__(self, name, sizeX, sizeY, keyUp, keyDown, keyL, keyR):
        self.name = name   
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.keyUp = keyUp
        self.keyDown = keyDown
        self.keyL = keyL
        self.keyR = keyR
        self.X = self._getRandomPosX()
        self.Y = self._getRandomPosY()
        self.speed = 5
        self.alive = True
        self.setColor()

    def setColor(self):

        min = 30
        max = 255

        # (255, 100, 0) (0, 128, 255)
        self.color = (rand.randint(min,max),rand.randint(min,max),rand.randint(min,max))

    def setRect(self, rect):
        self.rect = rect

    def _getRandomPosX(self):
        return rand.randint(spawnPadding, screenX-spawnPadding)

    def _getRandomPosY(self):
        return rand.randint(spawnPadding, screenY-spawnPadding)

    def isOutOfBounds(self):

        isOut = False

        if self.X + self.sizeX > screenX:
            self.X = screenX - self.sizeX
            isOut = True
        if self.X < 0:
            self.X = 0
            isOut = True
        if self.Y + self.sizeY > screenY:
            self.Y = screenY - self.sizeY
            isOut = True
        if self.Y < 0:
            self.Y = 0
            isOut = True

        return isOut

players.append(player("p1", 20, 20, pygame.K_UP,pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT))
players.append(player("p2", 20, 20, pygame.K_w,pygame.K_s, pygame.K_a, pygame.K_d))
players.append(player("p3", 20, 20, pygame.K_w,pygame.K_s, pygame.K_a, pygame.K_d))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            for p in players:
                p.setColor()

    pressed = pygame.key.get_pressed()

    screen.fill((0, 0, 0))

    for p in players:
        if not p.alive:
            p.setRect(pygame.draw.rect(screen, p.color, pygame.Rect(p.X, p.Y, p.sizeX, p.sizeY)))
            continue

        if pressed[p.keyUp]:
            p.Y -= p.speed
        if pressed[p.keyDown]:
            p.Y += p.speed
        if pressed[p.keyL]:
            p.X -= p.speed
        if pressed[p.keyR]:
            p.X += p.speed

        if p.isOutOfBounds():
            pass
            #p.alive = False
            #print(p.name, "is dead")

        p.setRect(pygame.draw.rect(screen, p.color, pygame.Rect(p.X, p.Y, p.sizeX, p.sizeY)))
        

    for p in players:
        if not p.alive:
            continue
        for pp in players:
            if p.name == pp.name:
                continue
            if pygame.sprite.collide_rect(p, pp):
                p.alive = False
                pp.alive = False
    
    allDead = False
    for p in players:
        if not p.alive:
            allDead = True
        else:
            allDead = False
            break
    if allDead:
        done = True



    pygame.display.flip()
    clock.tick(fps)
