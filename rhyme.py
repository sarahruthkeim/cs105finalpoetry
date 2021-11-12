import config


def two_words_rhyme(word1: str, word2: str) -> bool:
    """
    This functions takes two words as strings and returns True if they rhyme and False if they do not.

    :param word1: str, to be compared to word2
    :param word2: str, to be compared to word1
    :return: a boolean, True if word1 and word2 rhyme, False if they do not
    """
    if isinstance(word1, str) and isinstance(word2, str) and word1 != "" and word2 != "":  # preconditions (ensures both words are not empty and that they are both strs)
        lastvowel1 = ""  # instantiates variable that will hold the last vowel occuring in word1
        lastvowel2 = ""  # instantiates variable that will hold the last vowel occuring in word2
        for element in config.listofwords:  # goes through every list in
            if element[0] == word1:  # checks if the first element in the list is word1
                lastvowel1 = find_last_vowel(element)  # calls find_last_vowel for word1, which determines the last occuring vowel in the word, and sets that to lastvowel1
            elif element[0] == word2:  # checks if the first element in the list is word2
                lastvowel2 = find_last_vowel(element)  # calls find_last_vowel for word2, which determines the last occuring vowel in the word, and sets that to lastvowel2
            if lastvowel1 != "" and lastvowel2 != "":  # if the last vowel in both words have been found, breaks from the loop
                break
        if lastvowel1 == lastvowel2:  # checks if the last vowel in both words is the same
            return True  # if the vowels are the same, the words rhyme, return True
        else:
            return False  # the vowels are not the same, the words don't rhyme, return False
    else:
        raise Exception("Error. Please make sure word1 and word2 are of the string type and are not empty.")  # raises an exception and prints an error message if the preconditions are not met


def find_last_vowel(brokenword: list) -> str:
    """
    This function takes a list that is a word and its broken phonetic sounds and returns the last vowel sound that
    occurs in the word.

    :param brokenword: a list whose first element is a word and the subsequent elements, the word's phonetic spelling
    :return: a str that is the last vowel sound in the word
    """
    if isinstance(brokenword, list):  # preconditions (ensures brokenword is a list)
        vowels = ["AA", "AE", "AH", "AO", "AW", "AY", "EH", "ER", "EY", "IH", "IY", "UH", "UW"]  # a list of all possible vowels
        for index in reversed(brokenword):  # goes through every element in brokenword list starting from the last element
            if len(index) >= 3:  # checks if the length of the current element, a phonetic sound, is greater than or equal to 3
                if index[0:2] in vowels:  # checks if the first two chars in current element is in vowels (first two chars because some elements have numbers indiciating syllable stress, eliminates this problem)
                    return index[0:2]  # returns the fist two chars of current element if it appears in vowels
    else:
        raise Exception("Error. Please check that variable brokenword is of the correct type, list.")  # raises an exception and prints an error message if the preconditions are not met


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

print(convert_word("HELLO"))
print(convert_word("YELLOW"))

def perfect_vowel(word1: str, word2: str) -> bool:
    vowels = ["AA", "AE", "AH", "AO", "AW", "AY", "EH", "ER", "EY", "IH", "IY", "UH", "UW", "OW"]
    broken_word1 = convert_word(word1)
    broken_word2 = convert_word(word2)
    if broken_word1 == [0] or broken_word2 == [0]:
        raise Exception
    else:
        current_word1_vowel: str = ""
        current_word2_vowel: str = ""
        while current_word1_vowel == "" or current_word2_vowel == "":
            longest_word = max(len(broken_word1), len(broken_word2))
            for syllable_index in range(1, longest_word):
                current_word1_syllable = broken_word1[syllable_index][0:2]
                current_word2_syllable = broken_word2[syllable_index][0:2]
                if current_word1_syllable in vowels:
                    current_word1_vowel = current_word1_syllable
                    print(current_word1_vowel)
                if current_word2_syllable in vowels:
                    current_word2_vowel = current_word2_syllable
                    print(current_word2_vowel)
                if current_word1_vowel != "" and current_word2_vowel != "":
                    if current_word1_vowel != current_word2_vowel:
                        return False
                    else:
                        current_word1_syllable = ""
                        current_word2_syllable = ""
        return True
#

print(perfect_vowel("YELLOW", "AMERICA"))

