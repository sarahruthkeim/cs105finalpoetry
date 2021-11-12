from fileformatting import word_character_list



def two_words_rhyme(word1: str, word2: str, listofwords: list) -> str:
    lastvowel1 = ""
    lastvowel2 = ""
    for element in listofwords:
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


listofwords = word_character_list()
