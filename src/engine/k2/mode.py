import random, pygame, sys
from engine.common.deck import Deck
from engine.k2.patterns import PATTERNS

def run(screen):
    font = pygame.font.SysFont(None, 42)
    clock = pygame.time.Clock()
    deck = Deck()
    pattern_name, pattern_fn = random.choice(list(PATTERNS.items()))
    guesses, result = 0, "Press ENTER to deal 4 cards"

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT: pygame.quit(); sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE: return
                if e.key == pygame.K_RETURN:
                    hand = deck.draw(4)
                    guesses += 1
                    if pattern_fn(hand):
                        result = f"🎉 You found it! Pattern = {pattern_name}"
                        deck.reset()
                        guesses = 0
                        pattern_name, pattern_fn = random.choice(list(PATTERNS.items()))
                    else:
                        if guesses >= 3:
                            result = f"Out of guesses. It was: {pattern_name} — New round!"
                            deck.reset(); guesses = 0
                            pattern_name, pattern_fn = random.choice(list(PATTERNS.items()))
                        else:
                            result = f"Try again ({guesses}/3)"

        screen.fill((255,240,220))
        screen.blit(font.render("K-2 Mode (ESC to menu)", True, (40,40,40)), (32, 24))
        screen.blit(font.render(result, True, (30,110,30)), (32, 80))
        pygame.display.flip(); clock.tick(60)
