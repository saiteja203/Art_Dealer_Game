import sys, os
sys.path.append(os.path.dirname(__file__))

import pygame, sys as _sys
from engine.k2.mode import run as run_k2  

def menu():
    pygame.init()
    W, H = 1000, 700
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("Art Dealer Game")
    font = pygame.font.SysFont(None, 48)
    options = ["K-2 Mode", "Grades 3–5", "Grades 6–8", "Quit"]
    selected = 0
    clock = pygame.time.Clock()

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT: pygame.quit(); _sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key in (pygame.K_DOWN, pygame.K_s): selected = (selected+1) % len(options)
                if e.key in (pygame.K_UP,   pygame.K_w): selected = (selected-1) % len(options)
                if e.key in (pygame.K_RETURN, pygame.K_SPACE):
                    choice = options[selected]
                    if choice == "Quit": pygame.quit(); _sys.exit()
                    if choice == "K-2 Mode": run_k2(screen)
                    # elif choice == "Grades 3–5": run_k3_5(screen)
                    # elif choice == "Grades 6–8": run_k6_8(screen)

        screen.fill((245,245,245))
        title = font.render("Select Grade Level", True, (30,30,30))
        screen.blit(title, (W//2 - title.get_width()//2, 100))
        for i, label in enumerate(options):
            color = (0,120,215) if i == selected else (60,60,60)
            text = font.render(label, True, color)
            screen.blit(text, (W//2 - text.get_width()//2, 220 + i*70))
        pygame.display.flip(); clock.tick(60)

if __name__ == "__main__":
    menu()
