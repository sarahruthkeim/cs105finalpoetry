import config
import random


def two_words_rhyme(word1: str, word2: str) -> bool:
    """
    This functions takes two words as strings and returns True if they rhyme and False if they do not.

    :param word1: str, to be compared to word2
    :param word2: str, to be compared to word1
    :return: a boolean, True if word1 and word2 rhyme, False if they do not
    """
    if isinstance(word1, str) and isinstance(word2,
                                             str) and word1 != "" and word2 != "":  # preconditions (ensures both words are not empty and that they are both strs)
        last_vowel1 = ""  # instantiates variable that will hold the last vowel occurring in word1
        last_vowel2 = ""  # instantiates variable that will hold the last vowel occurring in word2
        for element in config.listofwords:  # goes through every list in
            if element[0] == word1:  # checks if the first element in the list is word1
                last_vowel1 = find_last_vowel(
                    element)  # calls find_last_vowel for word1, which determines the last occuring vowel in the word, and sets that to lastvowel1
            elif element[0] == word2:  # checks if the first element in the list is word2
                last_vowel2 = find_last_vowel(
                    element)  # calls find_last_vowel for word2, which determines the last occuring vowel in the word, and sets that to lastvowel2
            if last_vowel1 != "" and last_vowel2 != "":  # if the last vowel in both words have been found, breaks from the loop
                break  # breaks from the loop as soon as last_vowel1 and last_vowel2 are not empty strings
        if last_vowel1 == last_vowel2:  # checks if the last vowel in both words is the same
            return True  # if the vowels are the same, the words rhyme, return True
        else:
            return False  # the vowels are not the same, the words don't rhyme, return False
    else:
        raise Exception(
            "Error. Please make sure word1 and word2 are of the string type and are not empty.")  # raises an exception and prints an error message if the preconditions are not met


def find_last_vowel(broken_word: list) -> str:
    """
    This function takes a list that is a word and its broken phonetic sounds and returns the last vowel sound and the
    following consonant sounds that occur at the end of the word.

    :param broken_word: a list whose first element is a word and the subsequent elements, the word's phonetic spelling
    :return: a str that is the last vowel sound in the word and all the following consonants
    """
    if isinstance(broken_word, list):  # preconditions (ensures brokenword is a list)
        for index in reversed(
                broken_word):  # goes through every element in brokenword list starting from the last element
            if len(
                    index) >= 3:  # checks if the length of the current element, a phonetic sound, is greater than or equal to 3
                if index[
                   0:2] in config.vowels:  # checks if the first two chars in current element is in vowels (first two chars because some elements have numbers indiciating syllable stress, eliminates this problem)
                    vowel_to_end = index[
                                   0:2]  # removes the number that indicates syllable stress from the last vowel in brokenword
                    vowel_to_end += "".join(broken_word[broken_word.index(
                        index) + 1:])  # assigns the last vowel in brokenwords and all following consonants to vowel_to_end as a string with no spaces
                    return vowel_to_end  # returns the last vowel and subsequent consonants as a string with no spaces
    else:
        raise Exception(
            "Error. Please check that variable broken_word is of the correct type, list.")  # raises an exception and prints an error message if the preconditions are not met


def rhyme_suggestion(word_to_rhyme: str) -> str:
    """
    This function takes a word and returns a word that rhymes with the given word.

    :param word_to_rhyme: a str, word that will be compared to other words to see if they rhyme
    :return: str, a word that rhymes with word_to_rhyme, found in the CMU dictionary
    """
    assert (word_to_rhyme, str) and (" " not in word_to_rhyme), "Make sure that the word is a string and is only one word!"  # preconditions
    word_to_rhyme = word_to_rhyme.upper()
    index = random.randint(0, len(config.listofwords))
    for element in config.listofwords[index::]:
        if two_words_rhyme(element[0], word_to_rhyme) and element[0] != word_to_rhyme and element[0] not in config.possible_rhymes:
            config.possible_rhymes.append(element[0])
            return element[0]

rhyme_suggestion("rat")

def convert_word(word: str) -> list:
    """
    This function

    :param word:
    :return:
    """
    broken_word: list = []
    tracking = 0
    for index in range(len(config.listofwords)):
        if config.listofwords[index][0] == word:
            tracking += 1
            broken_word = config.listofwords[index]
    if tracking == 0:
        return [0]
    else:
        return broken_word


def perfect_vowel(word1: str, word2: str) -> bool:
    """"
    This function

    :param word1:
    :param word2:
    :return:
    """
    vowels = ["AA", "AE", "AH", "AO", "AW", "AY", "EH", "ER", "EY", "IH", "IY", "UH", "UW", "OW"]
    broken_word1 = convert_word(word1)
    broken_word2 = convert_word(word2)
