import random

hangmanASCII = ['''
 +---+
 |   |
     |
     |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
     |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
 |   |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\\  |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\\  |
/    |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\\  |
/ \\  |
     |
=========''']

# Dictionary of words and descriptions
words_dict = {
    "cat": "A small, furry animal that meows and likes to chase mice.",
    "dog": "A loyal animal that barks and enjoys running around.",
    "rabbit": "A fluffy creature with long ears that hops and eats carrots.",
    "bird": "A winged animal that flies and chirps.",
    "fish": "A water-dwelling animal that swims and has fins.",
    "elephant": "A very large animal with big ears and a long trunk.",
    "tiger": "A big, striped cat that roars and hunts.",
    "apple": "A round fruit that is usually red, green, or yellow.",
    "banana": "A yellow fruit that is long and curved.",
    "orange": "A round, orange-colored citrus fruit.",
    "grape": "A small, round fruit that grows in bunches on vines.",
    "pear": "A fruit that is green or yellow and shaped like a bell.",
    "kiwi": "A small, fuzzy brown fruit with green insides.",
    "carrot": "An orange vegetable that is long and crunchy.",
    "potato": "A brown vegetable that grows underground and is starchy.",
    "tomato": "A red fruit often mistaken for a vegetable.",
    "onion": "A vegetable with layers that can make you cry when cut.",
    "broccoli": "A green vegetable that looks like a tiny tree.",
    "spinach": "A leafy green vegetable used in salads and cooking.",
    "cucumber": "A long, green vegetable that is cool and watery.",
    "bag": "A container used to carry things, usually with handles.",
    "phone": "A device used to call or text people.",
    "book": "A collection of pages with words or pictures, used for reading.",
    "pen": "A tool for writing with ink.",
    "chair": "A piece of furniture for sitting on."
}

def main():
    # Choose a random word and its description from the dictionary
    hidden_word, description = random.choice(list(words_dict.items()))
    word_length = len(hidden_word)
    hidden_display = ['_'] * word_length
    counter = 0
    max_attempts = len(hangmanASCII) - 1
    guessed_letters = set()

    print("Welcome to Hangman!")

    while counter < max_attempts:
        print(hangmanASCII[counter])
        print("Word: " + " ".join(hidden_display))
        print(f"Hint: {description}")  # Display the description on each iteration
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}" if guessed_letters else "")

        guess = input("Guess a letter: ").strip().lower()

        # Checking if guess is one letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        # Revealing guessed letters
        if guess in hidden_word:
            print("Good guess!")
            for i in range(word_length):
                if hidden_word[i] == guess:
                    hidden_display[i] = guess
        else:
            print("Wrong guess!")
            counter += 1

        if '_' not in hidden_display:
            print("\nCongratulations! You Win! :) ")
            print("The word was:", hidden_word)
            return

    print(hangmanASCII[counter])
    print("Game over! You ran out of attempts. :( ")
    print("The word was:", hidden_word)


main()
