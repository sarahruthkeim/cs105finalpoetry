import config


def convert_word(word: str) -> list:
    """
    This function

    :param word:
    :return:
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


def remove_punctuation(current_line) -> list:
    """
    This function

    :return:
    """
    # variable list of all possible punctuation found in poem
    punctuation = [":", ";", '"', "(", ")", "!", ".", "?", "", ",", ]

    # for loop for each character in the punctuation list
    for char in punctuation:
        # replacing each punctuation mark found in the line with nothing
        current_line = current_line.replace(char, "")
    current_line = current_line.replace('-', '')

    # .upper function so words in line can be compatible with words from database
    current_line = current_line.upper()
    ordered_word_list = current_line.split(" ")
    return ordered_word_list


def identify_word_stress(current_word) -> str:
    """
    This function  .

    :param current_word:
    :return: 1 for stressed, 0 for unstressed
    """
    converted_word = convert_word(current_word)
    syllable_string = ''  # this will update as each syllable is found
    for syllable in converted_word:
        if syllable[0:2] in config.vowels:
            if syllable[2] == '0':  # no stress
                syllable_string += '0'
            elif syllable[2] == '1':  # stress is 1 (stressed)
                syllable_string += '1'
            elif syllable[2] == '2':  # secondary stress
                syllable_string += '2'
            else:  # tertiary stress
                syllable_string += '3'
    return syllable_string

# hello
