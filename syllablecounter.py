from config import vowels
from config import listofwords

def syllable_counter(words:str)-> int:
    """
    This function receives a word and counts the syllables in that word
    :param words: The inputted word
    :return: The # of syllables in that word
    """
    #Creating string of all the vowels
    #vowellist="AaEeIiOoUu"

    #Creating a syllable count for the given word
    syllablecount=0

    #special instances at the start of the word
    #if words[0] in vowels:
    #    syllablecount+=1
    #if words[0:2]=='Mc':
    #    syllablecount+=1

    #For loop for all the instances of syllables for all letters after the first letter in the word
    #for i in range(1, len(words)-1):

    #    if words[i] in vowels:
    #        syllablecount+=1
    #    if words[i] in vowels and words[i - 1] in vowels:
    #        syllablecount-=1
    #    if words[i] in vowels and words[i - 1] in vowels and words[i - 2] in vowels:
    #        syllablecount-=1
    #    if words[i]=="e" and words[i-1] not in vowels and words[i-2] in vowels:
    #        syllablecount-=1
    #    if words[i]=="y" and words[i-1] not in vowels and words[i+1] not in vowels:
    #        syllablecount+=1

    #Return the new syllable count
    #return syllablecount
    #print(syllablecount)


    for index in range(len(listofwords)):
        if listofwords[index][0] == words:
            for i in listofwords[index]:
                if i in vowels:
                    syllablecount+=1
            print(syllablecount)


syllable_counter('sparkle')
syllable_counter('submarine')
syllable_counter('ate')
syllable_counter('crucial')
syllable_counter('preach')
syllable_counter('preacher')
syllable_counter('antelope')