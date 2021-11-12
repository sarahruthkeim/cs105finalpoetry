def syllable_counter(words:str)-> int:
    vowels="AaEeIiOoUu"
    syllablecount=0
    if words[0] in vowels:
        syllablecount+=1
    for i in range(1, len(words)-1):
        #Other way of doing it. Don't know which way is better
        #if words[i] in vowels and words[i-1] not in vowels and words[i-2] not in vowels:
        #    syllablecount+=1
        #if words[i]=="E" or words[i]=="e" and words[i-1] not in vowels and words[i-2]:
            #syllablecount+=1
        #if words[i]=="e" or words[i]=="s" and words[i-1]=="e" or words[i-1]=="l" and words[i-2] not in vowels:
        #    syllablecount+=1

        if words[i] in vowels:
            syllablecount+=1
        if words[i] in vowels and words[i - 1] in vowels:
            syllablecount-=1
        if words[i] in vowels and words[i - 1] in vowels and words[i - 2] in vowels:
            syllablecount-=1
        if words[i]=="e" and words[i-1] not in vowels and words[i-2] in vowels:
            syllablecount-=1
        if words[i]=="y" and words[i-1] not in vowels and words[i+1] not in vowels
            syllablecount+=1
    return syllablecount


