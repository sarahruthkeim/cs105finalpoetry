from rhyme import two_words_rhyme
from config import listofwords

def user_interface():
    selection=int(input("Choose a function to use (1: Two words rhyming, 2:..."))
    #Two words rhyming function
    if selection==1:
        word1=str(input("Enter 1st word:"))
        word2=str(input("Enter 2nd word:"))
        two_words_rhyme(word1.upper(), word2.upper())

    #Perfect rhymes function
    if selection==2:

