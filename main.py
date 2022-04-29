import pygame, os, random
from Particle import Particle
pygame.init()
clock = pygame.time.Clock()

particles = []
particlesNum = 6

WIN_WIDTH, WIN_HEIGHT = 680, 680

WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Particle System")

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
        elif e.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for i in range(0, particlesNum):
                particles.append(Particle(x, y, WIN))
            pygame.mixer.Sound.play(pygame.mixer.Sound(os.path.join('sounds', str(random.randint(0, 4))+'.wav')))

	
    WIN.fill((200, 200, 200))
	
    for particle in particles:
        particle.update()
        particle.draw()
	
    clock.tick(30)
    pygame.display.update()