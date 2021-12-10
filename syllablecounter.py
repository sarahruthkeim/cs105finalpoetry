from config import vowels
from config import listofwords


def syllable_counter(words: str)-> int:
    """
    This function receives a word and counts the syllables in that word
    :param words: The inputted word
    :return: The # of syllables in that word
    """
    words=words.upper()

    #Creating a syllable count for the given word
    syllablecount=0

    #Return the new syllable count
    #return syllablecount
    #print(syllablecount)


    for index in range(len(listofwords)):
        if listofwords[index][0] == words:
            for i in listofwords[index]:
                if i[0:2] in vowels:
                    syllablecount+=1
            return syllablecount

# .......
syllable_counter('sparkle')
syllable_counter('submarine')
syllable_counter('ate')
syllable_counter('crucial')
syllable_counter('preach')
syllable_counter('preacher')
syllable_counter('antelope')

print(syllable_counter('SPARKLE'))