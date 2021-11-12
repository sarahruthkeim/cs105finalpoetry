from rhyme import two_words_rhyme
from syllablecounter import syllable_counter

num_of_lines = 0
user_poem_file = open("user_poem.txt", "r")
for line in user_poem_file:
    num_of_lines += 1

def haiku() -> bool:
    """

    :return:
    """
    if num_of_lines == 3:  # preconditions (checks that the poem has 3 lines as a haiku should)
        line_count = 1
        for line in user_poem_file:
            for word in line:
                total_syllables = total_syllables + syllable_counter(word)
            if line_count == 1 or line_count == 3:
                if total_syllables != 5:
                    return False
            elif line_count == 2:
                if total_syllables != 7:
                    return False
            line_count += 1
        return True
    else:
        raise Exception("Error. Poem should have three lines.")  # raises an exception if the preconditions are not met


def limerick() -> bool:
    """

    :return:
    """
    if num_of_lines == 5:  # preconditions (checks that the poem has 3 lines as a haiku should)
        line_count = 1
        list_of_lines = []
        for line in user_poem_file:
            words_in_line = line.split(" ")
            list_of_lines.append(words_in_line)
        if two_words_rhyme(list_of_lines[0][-1], list_of_lines[1][-1]):  # checks that the last word in lines 1 and 2 rhyme
            if two_words_rhyme(list_of_lines[1][-1], list_of_lines[4][-1]):  # checks that the last word in lines 2 and 5 rhyme (1 and 5 will rhyme if 1 and 2 do)
                if two_words_rhyme(list_of_lines[2][-1], list_of_lines[3][-1]):  # checks that the last word in lines 3 and 4 rhyme
                    return True  # the correct rhyming scheme of AABBA has been met, returns True
    else:
        raise Exception("Error. Poem should have three lines.")  # raises an exception if the preconditions are not met
