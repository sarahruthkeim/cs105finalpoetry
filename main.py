from rhyme import two_words_rhyme
import os

def user_interface():
    """
    This function interacts with you user and allows them to do many different functions relating to poems: checking
    that a user's poem matches the rhyming and syllable rules for a certain poetry style, providing a list of words that
    rhyme with a specific word, telling the user if two words do or do not rhyme,
    """
    selection = int(input("Choose a function to use - (1)two words rhyme, (2)write a poem to txt file, (3)check if poem matches a poetry style... : "))
    # Two words rhyming function
    if selection == 1:
        word1 = str(input("Enter 1st word:"))
        word2 = str(input("Enter 2nd word:"))
        print(two_words_rhyme(word1, word2))  # calls the two_words_rhyme function with the two words the user gives as input which will return whether or not the two words rhyme
    if selection == 2:
        user_poem_file = open("user_poem.txt", "w")  # opens and writes a text file called user_poem.txt under the variable name user_poem_file
        num_of_lines = int(input("How many lines does your poem have: "))  # asks the user how many lines there are in their poem and assigns their answer to num_of_lines
        for current_line in range(num_of_lines):  # iterates through the loop for however many lines are in the user's poem
            line = input(f"Write line {current_line + 1}: ")  # asks the user to write whatever the current line of the poem is and assigns it to line
            user_poem_file.write(line + "\n")  # writes the line the user just wrote to the user_poem_file
        user_poem_file.close()
    if selection == 3:
        try:
            import poetrystyles
            path = "/homes/skeim/PycharmProjects/cs105finalpoetry2/user_poem.txt"
            if os.path.exists(path):
                style_to_check = input("Type a number to check if your poem matches a specific style - (1) Haiku, (2) Limerick: ")
                if style_to_check == "1":
                    print(poetrystyles.haiku())
                elif style_to_check == "2":
                    print(poetrystyles.limerick())
        except FileNotFoundError:
            print("A file containing poetry does not exist. Please select option 2 and write your poem.")
            user_interface()





if __name__ == '__main__':
    user_interface()  # calls user_interface() function
    

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
