import random
import json

# Load word list from JSON files
with open('wordles.json', 'r') as f:
    WORD_LIST = json.load(f)  # Words that can be solutions

with open('nonwordles.json', 'r') as f:
    NON_WORD_LIST = json.load(f)  # Legal guesses but not solutions

# Combined set for fast lookup when validating guesses
VALID_GUESSES = set(WORD_LIST) | set(NON_WORD_LIST)

# ANSI color codes
GREEN = '\033[92m'
YELLOW = '\033[93m'
GRAY = '\033[90m'
WHITE = '\033[97m'
RESET = '\033[0m'

def get_feedback(guess, word):
    """
    Return feedback for a guess.
    Returns a list with: 🟩 (green - correct spot), 🟨 (yellow - wrong spot), ⬜ (gray - not in word)
    """
    feedback = ["⬜"] * 5
    word_letters = list(word)
    
    # First pass: mark greens
    for i in range(len(guess)):
        letter = guess[i]
        if letter == word[i]:
            feedback[i] = "🟩"
            word_letters[i] = None  # Mark as used
    
    # Second pass: mark yellows
    for i in range(len(guess)):
        if feedback[i] == "⬜" and letter in word_letters:
            feedback[i] = "🟨"
            word_letters[word_letters.index(letter)] = None  # Mark as used
    
    return feedback

def display_feedback(guess, feedback):
    """Display the guess with colored feedback."""
    return f"{' '.join(guess.upper())} - {' '.join(feedback)}"

def display_keyboard(letter_statuses):
    """Display alphabet with colored letters based on game state."""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    keyboard = []
    
    for letter in alphabet:
        if letter in letter_statuses:
            status = letter_statuses[letter]
            if status == 'green':
                keyboard.append(f"{GREEN}{letter.upper()}{RESET}")
            elif status == 'yellow':
                keyboard.append(f"{YELLOW}{letter.upper()}{RESET}")
            elif status == 'gray':
                keyboard.append(f"{GRAY}{letter.upper()}{RESET}")
        else:
            keyboard.append(f"{WHITE}{letter.upper()}{RESET}")
    
    return ' '.join(keyboard)

def play_wordle():
    """Main Wordle game loop."""
    word = random.choice(WORD_LIST).lower()
    attempts = 0
    max_attempts = 6
    guessed_words = []
    letter_statuses = {}  # Track: 'green', 'yellow', or 'gray' for each letter
    
    print("🎮 Welcome to Wordle!")
    print("Guess a 5-letter word. You have 6 attempts.\n")
    print("🟩 = Correct letter, correct spot")
    print("🟨 = Correct letter, wrong spot")
    print("⬜ = Letter not in word\n")
    
    while attempts < max_attempts:
        # Get player input
        guess = input(f"Attempt {attempts + 1}/{max_attempts}: ").lower().strip()
        
        # Validate input
        if len(guess) != 5 or not guess.isalpha():
            print("❌ Please enter a valid 5-letter word.\n")
            continue
        
        if guess not in VALID_GUESSES:
            print("❌ That word is not in the word list.\n")
            continue
        
        if guess in guessed_words:
            print("❌ You already guessed that word.\n")
            continue
        
        # Process guess
        guessed_words.append(guess)
        feedback = get_feedback(guess, word)
        print(display_feedback(guess, feedback))
        
        # Update letter statuses
        for i, letter in enumerate(guess):
            if feedback[i] == "🟩":
                letter_statuses[letter] = 'green'
            elif feedback[i] == "🟨":
                if letter not in letter_statuses or letter_statuses[letter] != 'green':
                    letter_statuses[letter] = 'yellow'
            elif feedback[i] == "⬜":
                if letter not in letter_statuses:
                    letter_statuses[letter] = 'gray'
        
        # Display keyboard
        print(display_keyboard(letter_statuses))
        print()
        
        # Check if player won
        if guess == word:
            print(f"\n🎉 You won in {attempts + 1} attempt(s)!")
            print(f"The word was: {word.upper()}")
            return
        
        attempts += 1
    
    # Player lost
    print(f"💔 Game Over! You ran out of attempts.")
    print(f"The word was: {word.upper()}")

if __name__ == "__main__":
    play_wordle()
