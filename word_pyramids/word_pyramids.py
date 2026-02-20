def print_star():
    print("*", end="")


def print_space():
    print(" ", end="")

def print_character(character):
    print(character, end="")

def rectangle(width, height):
    for row in range(height):
        for col in range(width):
            print_star()
        print()


def triangle_left(size):
    for row in range(size):
        for col in range(row + 1):
            print_star()
        print()


def triangle_right(size):
    for row in range(size):
        for col in range(size - row - 1):
            print_space()
        for col in range(row + 1):
            print_star()
        print()


def pyramid(size):
    for row in range(size):
        for col in range(size - row - 1):
            print_space()
        for col in range(2 * row + 1):
            print_star()
        print()

# Words
def word_triangle_left(word): 
    for row in range(len(word)):
        for col in range(row + 1):
            print_character(word[col])
        print()

def upside_word_triangle_left(word):
    for row in range(len(word)):
        for col in range(len(word) - row):
            print_character(word[col])
        print()

# Bonus ideas (can vary)
def upside_word_triangle_right(word):
    for row in range(len(word)):
        for col in range(row):
            print_space()
        for col in range(len(word) - row):
            print_character(word[col])
        print()

def reverse_rectangle(word):
    for row in range(len(word)):
        for col in range(len(word)):
            print_character(word[len(word) - col - 1])
        print()

def word_pyramid(word):
    for row in range(len(word)):
        for col in range(len(word) - row - 1):
            print_space()
        for col in range(row):
            print_character(word[len(word) - col - 1])
        for col in range(row + 1):
            print_character(word[col])
        print()

def main():
    # Star patterns:
    # rectangle(15, 3)
    # triangle_left(5)
    # triangle_right(5)
    # pyramid(7)

    # Character traits word patterns:
    # respect
    # responsibility
    # citizenship
    # leadership
    # caring
    # perseverance
    # fairness
    # honesty

    word_triangle_left("Respect")
    upside_word_triangle_left("Responsibility")
    upside_word_triangle_right("Citizenship")
    reverse_rectangle("Leadership")

    word_pyramid("Perseverance")
    character_traits = [
        "Respect",
        "Responsibility",
        "Citizenship",
        "Leadership",
        "Caring",
        "Perseverance",
        "Fairness",
        "Honesty"
    ]
    for trait in character_traits:
        word_pyramid(trait)


main()
