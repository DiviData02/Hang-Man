#Hangman Game

word = "Happy"
guessed_word = ["_"] * len(word)

guessed_letters = set()
attempts = 6

print("===> Welcome to Hangman Game <===")

while attempts > 0 and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Guessed Letters:", ", ".join(sorted(guessed_letters)))
    print("Attempts Left:", attempts)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in word:
        print("Correct!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong guess!")
        attempts -= 1

if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word.upper())
else:
    print("\nGame Over!")
    print("The correct word was:", word.upper())
