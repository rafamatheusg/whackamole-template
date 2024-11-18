import pygame
import random


def main():
    try:
        pygame.init()

        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()

        mole_x, mole_y = 0, 0


        def move_mole():
            nonlocal mole_x,mole_y
            col=random.randrange(0, 20)
            row=random.randrange(0, 16)
            mole_x=col*32
            mole_y=row*32

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mole_click = mole_image.get_rect(topleft=(mole_x, mole_y))
                    if mole_click.collidepoint(event.pos):
                        move_mole()


            screen.fill("light green")

            for x in range(0,640,32):
                pygame.draw.line(screen,"dark green",(x,0),(x,512))
            for y in range(0,512,32):
                pygame.draw.line(screen,"dark green",(0,y),(640,y))

            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
