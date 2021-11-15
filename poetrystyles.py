from rhyme import two_words_rhyme
from syllablecounter import syllable_counter

num_of_lines = 0
user_poem_file = open("user_poem.txt", "r")
for line in user_poem_file:
    num_of_lines += 1

def haiku() -> bool:
    """
    This function checks if a poem is a haiku by looking at the text in user_poem_file and returns True if each line
    fits the correct number of syllables according to the rules of a haiku and False if the lines do not match the
    correct number of syllables.

    :return: bool, True if correct syllable count for each line is met, False if they are not met
    """
    if num_of_lines == 3:  # preconditions (checks that the poem has 3 lines as a haiku should)
        line_count = 1  # instantiates variable line_count as int 1
        for line in user_poem_file:  # iterates through every line in user_poem_file
            for word in line:  # iterates through every word in the line
                total_syllables = total_syllables + syllable_counter(word)  # adds the number of syllables for the current word to the total number of syllables in the line
            if line_count == 1 or line_count == 3:  # checks if the current line is the first or the third line
                if total_syllables != 5:  # checks if the total_syllables for this line are not five
                    return False  # returns false if total_syllables is not five becuase a rule for a haiku have not been met
            elif line_count == 2:  # checks if the current line is the second line
                if total_syllables != 7:  # checks if the total_syllables for this line are seven
                    return False  # returns false if total_syllables is not seven because a rule for a haiku have not been met
            line_count += 1  # adds 1 to the line count
        return True  # returns True because all the lines met the correct syllable counts
    else:
        raise Exception("Error. Poem should have three lines.")  # raises an exception if the preconditions are not met


def limerick() -> bool:
    """
    This function checks if a poem is a limerick by looking at the text in user_poem_file and returns True if they fit
    the rhyming scheme for a limerick, AABBA, or False if they do not.

    :return: bool, True if rhyming scheme is met, False if it is not
    """
    if num_of_lines == 5:  # preconditions (checks that the poem has 3 lines as a haiku should)
        line_count = 1
        list_of_lines = []
        for line in user_poem_file:  # iterates through every line in user_poem_file
            words_in_line = line.split(" ")  # splits line into elements by " ", these elements become the list words_in_line
            list_of_lines.append(words_in_line)  # adds the list, words_in_line to another list, list_of_lines (list of lists)
        if two_words_rhyme(list_of_lines[0][-1], list_of_lines[1][-1]):  # checks that the last word in lines 1 and 2 rhyme
            if two_words_rhyme(list_of_lines[1][-1], list_of_lines[4][-1]):  # checks that the last word in lines 2 and 5 rhyme (1 and 5 will rhyme if 1 and 2 do)
                if two_words_rhyme(list_of_lines[2][-1], list_of_lines[3][-1]):  # checks that the last word in lines 3 and 4 rhyme
                    return True  # the correct rhyming scheme of AABBA has been met, returns True
    else:
        raise Exception("Error. Poem should have three lines.")  # raises an exception if the preconditions are not met
