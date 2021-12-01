def word_character_list():
    """
    This function takes the cmu pronouncing dictionary and returns a list whose elements are lists. The elements of
    these lists are a word and its broken phonetic parts/pronunciations. (basically a list of lists, each line in
    cmudict.txt is broken into a list)
    """
    word_list = []  # an empty list called word_list that will hold lists (a word and its broken phonetic parts)
    file_handle = open('cmudict.txt', 'r')  # opens and reads a text file called cmudict.txt and assigns it to the variable file_handle
    for line in file_handle:  # iterates through every line in file_handle
        if all(char.isalnum() or char.isspace() for char in line):
            modified_line = ""  # empty string, will become a modified version of the current line
            for char in range(len(line[:-1])):  # iterates through every character in the line (this for loop essentially removes the double spaces between phonetic elements in cmudict.txt)
                if line[char] + line[char + 1] != "  ":  # checks that the current character and the subsequent character are not "  " (2 spaces)
                    modified_line += line[char]  # adds the current character to the modified_line
            broken_word_list = modified_line.split(" ")  # makes each line a list, splitting elements by " " (a single space)
            word_list.append(broken_word_list)  # adds each line, now a list, to a list called word_list
    return word_list  # returns the list of lists, word_list



