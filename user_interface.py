from rhyme import two_words_rhyme


def user_interface():
    """
    This function interacts with you user
    """
    selection = int(input("Choose a function to use (1: Two words rhyming, 2:..."))
    # Two words rhyming function
    if selection == 1:
        word1 = str(input("Enter 1st word:"))
        word2 = str(input("Enter 2nd word:"))
        two_words_rhyme(word1, word2)
    if selection == 2:
        user_poem_file = open("user_poem.txt", "w")
        num_of_lines = int(input("How many lines does your poem have: "))
        for current_line in range(num_of_lines):
            line = input(f"Write line {current_line + 1}: ")
            user_poem_file.write(line + "\n")


user_interface()