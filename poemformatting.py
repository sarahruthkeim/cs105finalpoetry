import config

def convert_word(word: str) -> list:
    """

    :param word: word that is in the dictionary
    :return: Converts a word into a list of syllables that can be interpreted by other functions
    """
    brokenword: list = []
    tracking = 0
    for index in range(len(config.listofwords)):
        if config.listofwords[index][0] == word:
            tracking += 1
            brokenword = config.listofwords[index]
    if tracking == 0:
        return [0]
    else:
        return brokenword

def remove_punctuation(current_line: str) -> list:
    """
    :param current_line: current line of the poem being read, type is string
    :return: Removes punctuation from a provided line so that it can be interpreted by other functions.
    The line is also converted into a list of upper-case words.
    """
    #variable list of all possible punctuation found in poem
    punctuation = [":", ";", '"', "(", ")", "!", ".", "?", "", ",",]

    #for loop for each character in the punctuation list
    for char in punctuation:
        #replacing each punctuation mark found in the line with nothing
        current_line = current_line.replace(char, "")
    current_line = current_line.replace('-', '')

    #.upper function so words in line can be compatible with words from database
    current_line = current_line.upper()
    ordered_word_list = current_line.split(" ")
    return ordered_word_list


def identify_word_stress(current_word: str) -> str:
    """

    :param current_word: current line of the poem being read, type is string
    :return: Identifies the stress of a word by looking at each vowel in the word and creating a string that records the
    stress of the word as 0 (unstressed), 1 (primary stress), 2 (secondary stress), or 3 (tertiary stress)
    """
    converted_word = convert_word(current_word)
    syllable_string = '' # this will update as each syllable is found
    for syllable in converted_word:
        if syllable[0:2] in config.vowels:
            if syllable[2] == '0': # no stress
                syllable_string += '0'
            elif syllable[2] == '1':  # stress is 1 (stressed)
                syllable_string += '1'
            elif syllable[2] == '2': # secondary stress
                syllable_string += '2'
            else:  # tertiary stress
                syllable_string += '3'
    return syllable_string

# hello
