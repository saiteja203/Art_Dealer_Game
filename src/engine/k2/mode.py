import random, pygame, sys
from engine.common.deck import Deck
from engine.k2.patterns import PATTERNS

#card drawing helpers
SUIT_SYMBOLS = {"hearts": "♥", "diamonds": "♦", "clubs": "♣", "spades": "♠"}
SUIT_COLOR = {
    "hearts": (200, 0, 0), "diamonds": (200, 0, 0),
    "clubs": (0, 0, 0), "spades": (0, 0, 0),
}

def draw_card(surface, x, y, w, h, card, font_rank, font_suit):
    # shadow
    pygame.draw.rect(surface, (0, 0, 0), (x+4, y+6, w, h), border_radius=10)
    # card background
    pygame.draw.rect(surface, (255, 255, 255), (x, y, w, h), border_radius=10)
    # border
    pygame.draw.rect(surface, (40, 40, 40), (x, y, w, h), width=2, border_radius=10)

    suit = SUIT_SYMBOLS.get(card.suit, "?")
    color = SUIT_COLOR.get(card.suit, (0, 0, 0))

    # rank & suit (top-left)
    rank_txt = font_rank.render(card.rank, True, color)
    suit_txt = font_suit.render(suit, True, color)
    surface.blit(rank_txt, (x + 10, y + 8))
    surface.blit(suit_txt, (x + 10, y + 36))

    # big centered suit
    big = font_rank.render(suit, True, color)
    surface.blit(big, (x + w//2 - big.get_width()//2, y + h//2 - big.get_height()//2))

    # rank & suit (bottom-right)
    surface.blit(rank_txt, (x + w - rank_txt.get_width() - 10, y + h - rank_txt.get_height() - 34))
    surface.blit(suit_txt, (x + w - suit_txt.get_width() - 10, y + h - suit_txt.get_height() - 8))


def run(screen):
    # UI fonts
    font = pygame.font.SysFont(None, 42)
    small = pygame.font.SysFont(None, 28)
    # DejaVu usually has suit glyphs
    font_rank = pygame.font.SysFont("DejaVu Sans", 48)
    font_suit = pygame.font.SysFont("DejaVu Sans", 36)

    clock = pygame.time.Clock()
    deck = Deck()

    # audio- win sound
    try:
        pygame.mixer.init()
        win_snd = pygame.mixer.Sound("assets/audio/win.wav")
    except Exception:
        win_snd = None

    # hidden pattern for the round
    pattern_name, pattern_fn = random.choice(list(PATTERNS.items()))
    guesses = 0
    status = "Press ENTER to deal 4 cards"
    last_hand = []
    win_frames = 0 

    def new_round(msg="New round! Press ENTER to deal 4 cards"):
        nonlocal pattern_name, pattern_fn, guesses, last_hand, status
        deck.reset()
        guesses = 0
        last_hand = []
        pattern_name, pattern_fn = random.choice(list(PATTERNS.items()))
        status = msg

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    return  # back to menu
                # R = manual new round (disabled during win animation)
                if e.key == pygame.K_r and win_frames == 0:
                    new_round()
                # ENTER = deal/evaluate (disabled during win animation)
                if e.key == pygame.K_RETURN and win_frames == 0:
                    if len(deck._cards) < 4:
                        deck.reset()
                    last_hand = deck.draw(4)
                    guesses += 1

                    if pattern_fn(last_hand):
                        status = f"🎉 You found it! Pattern = {pattern_name}"
                        win_frames = 120
                        if win_snd:
                            try: win_snd.play()
                            except Exception: pass
                    else:
                        if guesses >= 3:
                            status = f"Out of guesses. It was: {pattern_name}"
                            new_round(msg="Press ENTER to deal 4 cards")
                        else:
                            status = f"Try again ({guesses}/3)"

        # after win animation, start fresh (single reset path)
        if win_frames > 0:
            win_frames -= 1
            if win_frames == 0:
                new_round()

        # --- draw UI ---
        screen.fill((255, 240, 220))
        screen.blit(font.render("K-2 Mode (ESC to menu)", True, (40, 40, 40)), (32, 20))
        screen.blit(font.render(status, True, (30, 110, 30)), (32, 70))
        screen.blit(small.render("Find the dealer's pattern!", True, (60, 60, 60)), (32, 110))

        # guesses left + footer controls
        guesses_left = max(0, 3 - guesses)
        screen.blit(small.render(f"Guesses left: {guesses_left}", True, (80, 80, 80)), (32, 136))
        footer = small.render("ENTER: Deal   R: New Round   ESC: Menu", True, (60, 60, 60))
        screen.blit(footer, (32, screen.get_height() - 48))

        # card area
        CARD_W, CARD_H = 120, 170
        gap = 24
        total_w = 4 * CARD_W + 3 * gap
        start_x = screen.get_width() // 2 - total_w // 2
        y_cards = 170

        # highlight during win anim
        if win_frames > 0 and last_hand:
            pygame.draw.rect(
                screen, (255, 230, 120),
                (start_x - 8, y_cards - 8, total_w + 16, CARD_H + 16),
                width=6, border_radius=14
            )

        # draw dealt cards
        for i, c in enumerate(last_hand):
            x = start_x + i * (CARD_W + gap)
            draw_card(screen, x, y_cards, CARD_W, CARD_H, c, font_rank, font_suit)

        # confetti
        if win_frames > 0:
            import random as _r
            for _ in range(120):
                pygame.draw.circle(
                    screen,
                    (_r.randint(0, 255), _r.randint(0, 255), _r.randint(0, 255)),
                    (_r.randint(0, screen.get_width()), _r.randint(0, screen.get_height())),
                    2
                )

        pygame.display.flip()
        clock.tick(60)
