from config import listofwords
from config import vowels

def syllable_counter(words:str)-> int:
    """
    This function receives a word and counts the syllables in that word
    :param words: The inputted word
    :return: The # of syllables in that word
    """
    #syllabe count variable to keep count of syllables in word
    syllablecount=0

    #for loop checking to see if word inputted in function in list of words
    for index in range(len(listofwords)):
        if listofwords[index][0]==words:

            #for loop checking to see if vowels are in phoenetic spelling of word and adding to syllable count if so
            for i in listofwords[index]:
                if i[0:2] in vowels:
                    syllablecount+=1

            #return(syllablecount)
            print(syllablecount)

syllable_counter('SPARKLE')
syllable_counter('SUBMARINE')
syllable_counter('ATE')
syllable_counter('CRUCIAL')
syllable_counter('PREACH')
syllable_counter('PREACHER')