def word_character_list():
    file_handle = open('cmudict.txt', 'r')
    list_of_lists = []
    for line in file_handle:
        current_line = line[:-1]
        modified_line = current_line.replace("  ", " ")
        list_of_lists += [modified_line.split(" ")]
    return list_of_lists

test_list = word_character_list()

def find_word(list_of_lists, user_word: str) -> list:
    for line_list in range(len(list_of_lists)):
        if list_of_lists[line_list][0] == user_word:
            return list_of_lists[line_list]

print(find_word(test_list, 'WORD'))


# This is the old version of perfect_rhyme()

def perfect_vowel(word1: str, word2: str) -> bool:
    vowels = ["AA", "AE", "AH", "AO", "AW", "AY", "EH", "ER", "EY", "IH", "IY", "UH", "UW", "OW"]
    broken_word1 = convert_word(word1)
    broken_word2 = convert_word(word2)
    if broken_word1 == [0] or broken_word2 == [0]:
        raise Exception
    else:
        if len(broken_word1) != len(broken_word2):
            return False
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