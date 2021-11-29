import config

def convert_word(word: str) -> list:
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

    :return:
    """
    punctuation = [":", ";", '"', "(", ")", "!", ".", "?", "", ","]
    for char in punctuation:
        current_line = current_line.replace(char, "")
    current_line = current_line.upper()
    ordered_word_list = current_line.split(" ")
    return ordered_word_list

def identify_word_stress(current_word) -> str:
    """

    :param current_line:
    :return: 1 for stressed, 0 for unstressed
    """
    converted_word = convert_word(current_word)
    syllable_string = '' # this will update as each syllable is found
    for syllable in converted_word:
        if syllable[0:2] in config.vowels:
            if syllable[2] == '0':  # stress is 0 (unstressed)
                syllable_string += "0"
            else:  # stress is 1, 2, or 3 (stressed)
                syllable_string += "1"
    return syllable_string

print(identify_word_stress('HELLO'))
print(identify_word_stress('MADAGASCAR'))

def iambic_pentameter() -> bool:
    for line in user_poem_file:
        formatted_line = remove_punctuation(line[:-1])
        total_syllables = 0
        syllable_mask = ''
        for word in formatted_line:
            syllable_mask += identify_word_stress(word)
            total_syllables += syllablecounter(word)
        if total_syllables != 10 or syllable_mask != '0101010101':  # 0101010101 = unstressed, stressed, unstressed, stressed, ...
            return False
    return True
