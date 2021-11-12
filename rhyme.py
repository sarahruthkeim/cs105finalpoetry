import config


def two_words_rhyme(word1: str, word2: str) -> str:
    lastvowel1 = ""
    lastvowel2 = ""
    for element in config.listofwords:
        if element[0] == word1:
            lastvowel1 = find_last_vowel(element)
        elif element[0] == word2:
            lastvowel2 = find_last_vowel(element)
        if lastvowel1 != "" and lastvowel2 != "":
            break
    if lastvowel1 == "" or lastvowel2 == "":
        return "One or both of these words did not appear in the dictionary."
    elif lastvowel1 == lastvowel2:
        return "These words rhyme."
    else:
        return "These words do not rhyme."


def find_last_vowel(brokenword: list) -> str:
    vowels = ["AA", "AE", "AH", "AO", "AW", "AY", "EH", "ER", "EY", "IH", "IY", "UH", "UW"]
    for index in reversed(brokenword):
        if len(index) >= 3:
            if index[0:2] in vowels:
                return index[0:2]


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

print(convert_word("TEST"))

def perfect_vowel(word1: str, word2: str) -> bool:
    vowels = ["AA", "AE", "AH", "AO", "AW", "AY", "EH", "ER", "EY", "IH", "IY", "UH", "UW"]
    broken_word1 = convert_word(word1)
    broken_word2 = convert_word(word2)
    if broken_word1 == [0] or broken_word2 == [0]:
        raise Exception
    else:
        if len(broken_word1) > len(broken_word2):
            current_word1_syllable: str = ""
            current_word2_syllable: str = ""
            for syllable_index in range(1, len(convert_word(word2))):
                while current_word1_syllable == "" or current_word2_syllable == "":
                    if broken_word1[syllable_index][0:1] in vowels:
                        current_word1_syllable = broken_word1[syllable_index][0:1]
                        print(current_word1_syllable)
                    if word2[syllable_index][0:1] in vowels:
                        current_word2_syllable = broken_word2[syllable_index][0:1]
                        print(current_word2_syllable)
                    if current_word1_syllable != "" and current_word2_syllable != "":
                        if current_word1_syllable != current_word2_syllable:
                            return False
                        else:
                            current_word1_syllable = ""
                            current_word2_syllable = ""
                            break
            return True


print(perfect_vowel("SERENDIPITY", "HELLO"))

