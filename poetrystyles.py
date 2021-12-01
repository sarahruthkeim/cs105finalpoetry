from rhyme import two_words_rhyme
from syllablecounter import *
from poemformatting import *

num_of_lines = 0  #
user_poem_file = open("user_poem.txt", "r")  #
for line in user_poem_file:  #
    num_of_lines += 1  #

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
            cleaned_line = remove_punctuation(line)
            for word in cleaned_line:  # iterates through every word in the cleaned_line list
                total_syllables = total_syllables + syllable_counter(word)  # adds the number of syllables for the current word to the total number of syllables in the line
            if line_count == 1 or line_count == 3:  # checks if the current line is the first or the third line
                if total_syllables != 5:  # checks if the total_syllables for this line are not five
                    user_poem_file.close()
                    return False  # returns false if total_syllables is not five becuase a rule for a haiku have not been met
            elif line_count == 2:  # checks if the current line is the second line
                if total_syllables != 7:  # checks if the total_syllables for this line are seven
                    user_poem_file.close()
                    return False  # returns false if total_syllables is not seven because a rule for a haiku have not been met
            line_count += 1  # adds 1 to the line count
        user_poem_file.close()
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
                    user_poem_file.close()
                    return True  # the correct rhyming scheme of AABBA has been met, returns True
        user_poem_file.close()
        return False
    else:
        raise Exception("Error. Poem should have three lines.")  # raises an exception if the preconditions are not met


def iambic_pentameter() -> bool:
    """

    :return: This function looks at user_poem.txt and checks to see if it is iambic pentameter. There are two parts to
    Iambic Pentameter. The "Iambic" part specifies that syllables must alternate as unstressed and stressed (this means
    how much emphasis is placed on each syllable when read aloud). The "Pentameter" part specifies tha there must be
    10 syllables per line. If the function identifies a line that doesn't have 10 syllables, it returns False. The
    function is slightly more flexible for the Iambic requirement. It records how many syllables do not fit the correct
    scheme, and if this amount gets too high it returns False. If neither of these conditions happen, the function
    returns True.

    Some problems with this function: Shakespeare is the most well known user of this poetry style, but this function
    cannot analyze his poetry since he uses antiquated English. Many of the words he uses are not in the dictionary.

    Also, poets frequenetly bend the rules and force words to fit the Iambic pattern through the way they are read.
    This function pretty much always returns false because of this, as it is difficult for computers to identify the
    nuance of words being able to be read in multiple ways. Machine-learning would be a good solution to this, but
    that is well beyond our ability to code.
    """
    wrong_syllables: int = 0  # the number of wrong syllables will be kept track of with this variable
    file_handle = open('user_poem.txt', 'r')
    for line in file_handle:
        formatted_line = remove_punctuation(line[:-1]) # calls function remove_punctuation from poemformatting.py, this
        # allows each word to be interpreted by the other functions called in this code
        total_syllables = 0
        syllable_mask = ''  # this will record the pattern of stresses for each line, reset to a blank string each time
        # a new line is read
        for word in formatted_line:
            syllable_mask += identify_word_stress(word)  # calls function identify_word_stress from poemformatting.py
            total_syllables += syllable_counter(word)
        if total_syllables != 10:  # pentameter condition
            return False
        for index in range(1, len(syllable_mask)):
            if index % 2 == 0:  # syllables at even position (2nd syllable, 4th syllable, ...)
                if syllable_mask[index] != '1':  # stressed syllables
                    wrong_syllables += 1
            else:  # syllables at odd position (1st syllable, 3rd syllable, ...)
                if syllable_mask[index] == '1':  # unstressed syllables
                    wrong_syllables += 1
    file_handle.close()
    if wrong_syllables > num_of_lines * 2:  # iambic condition, maximum of two incorrect syllables allowed per line
        return False
    else:
        return True

def sonnet() -> bool:
    if num_of_lines != 14:
        return False
    else:
        file_handle = open('user_poem.txt', 'r')
        line_tracker = 0
        for line in file_handle:
            line_tracker += 1
            if line_tracker % 4 == 0:

            if line_tracker == 14:


def poem_type() -> str:
    if sonnet() == True:
        return 'sonnet'
    if haiku() == True:
        return 'haiku'
    if limerick() == True:
        return 'limerick'
    if iambic_pentameter() == True:
        return 'iambic_pentameter'
    else:
        return 'freeverse'


