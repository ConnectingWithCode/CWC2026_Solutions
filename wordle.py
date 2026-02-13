import random
import json

# Load word list from JSON file
with open('wordles.json', 'r') as f:
    WORD_LIST = json.load(f)
    WORD_SET = set(WORD_LIST)  # For fast lookup when validating guesses

def get_feedback(guess, word):
    """
    Return feedback for a guess.
    Returns a list with: 🟩 (green - correct spot), 🟨 (yellow - wrong spot), ⬜ (gray - not in word)
    """
    feedback = ["⬜"] * 5
    
    # First pass: mark greens
    for i in range(len(guess)):
        letter = guess[i]
        if letter == word[i]:
            feedback[i] = "🟩"
    
    # Second pass: mark yellows
    for i in range(len(guess)):
        letter = guess[i]
        if feedback[i] == "⬜" and letter in word:
            feedback[i] = "🟨"
    
    return feedback

def display_feedback(guess, feedback):
    """Display the guess with colored feedback."""
    return f"{' '.join(guess.upper())} - {' '.join(feedback)}"

def play_wordle():
    """Main Wordle game loop."""
    word = random.choice(WORD_LIST).lower()
    attempts = 0
    max_attempts = 6
    guessed_words = []
    
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
        
        if guess not in WORD_SET:
            print("❌ That word is not in the word list.\n")
            continue
        
        if guess in guessed_words:
            print("❌ You already guessed that word.\n")
            continue
        
        # Process guess
        guessed_words.append(guess)
        feedback = get_feedback(guess, word)
        print(display_feedback(guess, feedback))
        
        # Check if player won
        if guess == word:
            print(f"\n🎉 You won in {attempts + 1} attempt(s)!")
            print(f"The word was: {word.upper()}")
            return
        
        attempts += 1
        print()
    
    # Player lost
    print(f"💔 Game Over! You ran out of attempts.")
    print(f"The word was: {word.upper()}")

if __name__ == "__main__":
    play_wordle()
