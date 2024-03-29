from rhyme import two_words_rhyme
from rhyme import find_last_vowel
from syllablecounter import *
from poemformatting import *

num_of_lines = 0
list_of_lines = []
user_poem_file = open("user_poem.txt", "r")
for line in user_poem_file:
    list_of_lines.append(line)
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
        total_syllables=0
        file_handle=open('user_poem.txt', 'r')
        lines = file_handle.readlines()
        for line in lines:
            print(line)
        for line in file_handle:  # iterates through every line in user_poem_file
            cleaned_line = remove_punctuation(line[:-1])
            for word in cleaned_line:  # iterates through every word in the cleaned_line list
                total_syllables = total_syllables + syllable_counter(word)  # adds the number of syllables for the current word to the total number of syllables in the line
            if line_count == 1 or line_count == 3:  # checks if the current line is the first or the third line
                if total_syllables != 5:  # checks if the total_syllables for this line are not five
                    file_handle.close()
                    return False  # returns false if total_syllables is not five becuase a rule for a haiku have not been met
            elif line_count == 2:  # checks if the current line is the second line
                if total_syllables != 7:  # checks if the total_syllables for this line are seven
                    file_handle.close()
                    return False  # returns false if total_syllables is not seven because a rule for a haiku have not been met
            line_count += 1  # adds 1 to the line count
        file_handle.close()
        return True  # returns True because all the lines met the correct syllable counts
    else:
        return False


def limerick() -> bool:
    """
    This function checks if a poem is a limerick by looking at the text in user_poem_file and returns True if they fit
    the rhyming scheme for a limerick, AABBA, and the correct syllable structure, or False if they do not.

    :return: bool, True if rhyming scheme and syllable structure are met, False if it does not
    """
    if num_of_lines == 5:  # preconditions (checks that the poem has 5 lines as a limerick should)
        line_number = 1  # initializing line_number as the first line
        broken_line = []  # a list that will hold the words of a given line in a list
        to_check_ryhme = []  # a list of lists which are the words of a line
        for line in list_of_lines:  # iterates through every line in user_poem_file
            syllable_total = 0  # initializing total syllables in a line to zero
            line = line.strip()  # removes /n from line
            broken_line = remove_punctuation(line)  # removes all punctuation from line so syllable counter will work correctly
            to_check_ryhme.append(broken_line)  # adds the cleaned line, in its broken word form as a list to another list, to_check_rhyme
            for word in broken_line:  # iterates through every word in a line
                syllable_total = syllable_total + syllable_counter(word)  # counts the number of syllables for every word and adds it to a line total
            if line_number == 1 or line_number == 2 or line_number == 5:   # if it is line, 1, 2, or 5, sees if total sylables are between 7 and 10
                if not 7 <= syllable_total <= 10:
                    return False  # if it does not meet the syllable requirements, automatically returns False
            elif line_number == 3 or line_number == 4:  # if it is line 3 or 4, sees if total syllables are between 5 and 7
                if not 5 <= syllable_total <= 7:
                    return False  # if it does not meet the syllable requirements, automatically returns False
            line_number += 1  # adds one to the line number, goes to the next line
        if two_words_rhyme(to_check_ryhme[0][-1], to_check_ryhme[1][-1]):  # checks that the last word in lines 1 and 2 rhyme
            if two_words_rhyme(to_check_ryhme[1][-1], to_check_ryhme[4][-1]):  # checks that the last word in lines 2 and 5 rhyme (1 and 5 will rhyme if 1 and 2 do)
                if two_words_rhyme(to_check_ryhme[2][-1], to_check_ryhme[3][-1]):  # checks that the last word in lines 3 and 4 rhyme
                    return True  # the correct rhyming scheme of AABBA has been met, returns True
        return False
    else:
        return False  # returns False if preconditions are not met


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
        for index in range(len(syllable_mask)):
            if index % 2 != 0:  # syllables at even position (2nd syllable, 4th syllable, ...)
                if syllable_mask[index] != '1':  # stressed syllables
                    wrong_syllables += 1
            else:  # syllables at odd position (1st syllable, 3rd syllable, ...)
                if syllable_mask[index] == '1':  # unstressed syllables
                    wrong_syllables += 1
        print(syllable_mask)
        print(f'{wrong_syllables} wrong syllables identified')
    file_handle.close()
    if wrong_syllables > num_of_lines * 3:  # iambic condition, maximum of three incorrect syllables allowed per line
        return False
    else:
        return True

def sonnet() -> bool:
    """

    :return: checks to see if user's poem is a sonnet. Returns True if it is and False if it is not. A sonnet has the
    rhyme scheme ABABCDCDEFEFGG, this is what will be used to determine if it is a sonnet or not.
    """
    if num_of_lines != 14:  # poem must have 14 lines for it to possibly be a sonnet.
        return False
    else:
        file_handle = open('user_poem.txt', 'r')
        line_tracker = 0  # variable keeps track of the line being checked
        formatted_line_list = []  # variable is a list of lists. First list is each line, lists within this list are the
        # words of each line.
        for line in file_handle:
            formatted_line_list += [remove_punctuation(line[:-1])]  # remove_punctuation called from poemformatting.py.
            # A description of what this function does is written there.
            line_tracker += 1
            if line_tracker % 4 == 0:  # sonnet rhyme scheme repeats every 4 lines, so this code checks the rhyme scheme
                # every 4 lines.
                line1_word = formatted_line_list[line_tracker - 4][-1]  # each variable represents the last word of each
                # line. These will be used to check if two lines rhyme.
                line2_word = formatted_line_list[line_tracker - 3][-1]
                line3_word = formatted_line_list[line_tracker - 2][-1]
                line4_word = formatted_line_list[line_tracker - 1][-1]
                if two_words_rhyme(line1_word, line3_word) != True:  # if line 1 and 3 do not rhyme, the rhyme scheme is
                    # broken, so False is returned and the function stops.
                    return False
                if two_words_rhyme(line2_word, line4_word) != True:  # same thing is done for lines 2 and 4.
                    return False
            if line_tracker == 14:  # lines 13 and 14 have a unique rhyme scheme "GG", so new code is required.
                line13_word = formatted_line_list[12][-1]
                line14_word = formatted_line_list[13][-1]
                if two_words_rhyme(line13_word, line14_word) != True:
                    return False
    file_handle.close()
    return True  # if the code goes through the entire poem without finding an error, True is returned.

def identify_rhyme_scheme() -> str:
    """

    :return: records the rhyme scheme of the poem as a string. Normally, the first line is marked as "A", and all
    subsequent lines that rhyme with are also marked as A. The same is done for the next unique rhyme, recording it as
    "B". However, in this code the alphabet letter is attached to the position of the last instance of a rhyme. For
    example, the sonnet rhyme scheme should normally be "ABABCDCDEFEFGG", but in this case it would be "CDCDGHGHKLKLNN".
    """
    file_handle = open('user_poem.txt', 'r')
    alphabet_letters = 'ABCDEFGHIJKLMNOPQRZTUVWXYZ'
    rhyme_list = []  # this list will be appended for each line, storing the last syllable of each line.
    for line in file_handle:
        current_line = remove_punctuation(line[:-1])
        current_word = convert_word(current_line[-1])
        rhyme_list += [find_last_vowel(current_word)]
    rhyme_pattern = ['0'] * len(rhyme_list)  # blank list the size of the number of lines in the poem
    for i in range(len(rhyme_list)):
        for j in range(i, len(rhyme_list)):
            if rhyme_list[i] == rhyme_list[j]:  # if two words have the same rhyme...
                rhyme_pattern[i] = alphabet_letters[j]  # they are recorded with the same alphabet letter.
    file_handle.close()
    final_pattern = ''
    for element in rhyme_pattern:
        final_pattern += element  # list is converted back into a string.
    return final_pattern


def poem_type() -> str:
    """

    :return: this function checks the user's poem to see if it matches the format of any of the rhyme schemes definied.
    If none of these rhyme schemes are identified, the poem is declared to be "freeverse".
    """
    if sonnet() == True and iambic_pentameter() == True:
        return 'english sonnet'  # in an English sonnet, the poem must fit both the sonnet rhyme scheme and the iambic
        # pentameter meter.
    elif sonnet() == True:
        return 'sonnet'
    elif iambic_pentameter() == True:
        return 'iambic pentameter'
    elif haiku() == True:
        return 'haiku'
    elif limerick() == True:
        return 'limerick'
    else:
        return 'freeverse'
