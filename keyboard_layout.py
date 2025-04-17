import pygame

# Define colors
GREY_BACKGROUND = (50, 50, 50)  # Dark grey background
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 20, 60)  # Red for selected key

# Increase spacing to match bigger keyboard
keys = "QWERTYUIOPASDFGHJKLZXCVBNM"
key_positions = {key: ((i % 10) * 140 + 50, (i // 10) * 150 + 100) for i, key in enumerate(keys)}  # Shift down to make space for title

def draw_keyboard(screen, selected_key):
    screen.fill(GREY_BACKGROUND)  # Set grey background

    # Draw "Trinetra" text at the top
    font_title = pygame.font.Font(None, 80)  # Larger font for title
    title_text = font_title.render("Trinetra", True, WHITE)
    screen.blit(title_text, (screen.get_width() // 2 - 100, 20))  # Centered title

    for key, pos in key_positions.items():
        color = RED if key == selected_key else BLACK  # Red for selected key, black for others
        pygame.draw.rect(screen, color, (pos[0], pos[1], 120, 120), border_radius=10)  # Rounded keys
        pygame.draw.rect(screen, WHITE, (pos[0], pos[1], 120, 120), 2, border_radius=10)  # White border

        # Draw text inside key
        font = pygame.font.Font(None, 60)
        text = font.render(key, True, WHITE)  # White text for contrast
        screen.blit(text, (pos[0] + 40, pos[1] + 35))

    pygame.display.flip()
