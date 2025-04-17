import pygame
import time
import webbrowser
from spellchecker import SpellChecker
from keyboard_layout import draw_keyboard

# Initialize spell checker
spell = SpellChecker()

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((1600, 600))  # Bigger keyboard
pygame.display.set_caption("Gaze Keyboard")

gaze_threshold = 2.0  # Stability time before selecting a key
cooldown_time = 3.0  # Prevents fast re-selection
last_typed_time = 0
gaze_start_time = None
selected_letter = None

typed_letters = ""  # Stores selected letters
letter_limit = 5  # Limit gaze selection to 5 letters

def process_text(raw_text):
    """ Uses PySpellChecker to correct words before searching. """
    words_list = raw_text.split()  # Split by space
    corrected_words = [spell.correction(word) or word for word in words_list]  # Correct spelling
    return " ".join(corrected_words)  # Return corrected sentence

while True:
    # Check if letter limit is reached
    if len(typed_letters) >= letter_limit:
        processed_query = process_text(typed_letters)  # NLP processing

        screen.fill((255, 255, 255))  # White background
        font = pygame.font.Font(None, 80)
        text = font.render(f"Searching: {processed_query}", True, (255, 0, 0))
        screen.blit(text, (500, 250))
        pygame.display.flip()

        search_url = f"https://www.google.com/search?q={processed_query}"
        webbrowser.open(search_url)  # Open Google search
        time.sleep(3)  # Wait for a few seconds before exiting
        pygame.quit()
        exit()

    # Simulate gaze selection (For testing, cycle through keys every 2 seconds)
    simulated_keys = list("QWERTYUIOPASDFGHJKLZXCVBNM")
    current_time = time.time()
    
    if gaze_start_time is None or current_time - gaze_start_time > gaze_threshold:
        selected_letter = simulated_keys[int(time.time()) % len(simulated_keys)]
        gaze_start_time = current_time
        print(selected_letter, end='', flush=True)  # Simulate typing
        typed_letters += selected_letter  # Add letter to search query

    # Draw keyboard
    draw_keyboard(screen, selected_letter)

    # Process Pygame events to prevent freezing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
