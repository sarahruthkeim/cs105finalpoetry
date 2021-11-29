def remove_punctuation(current_line) -> list:
    """

    :return: This function checks to see if a line is iambic pentameter or not
    """
    #variable list of all possible punctuation found in poem
    punctuation = [":", ";", '"', "(", ")", "!", ".", "?", "", ","]

    #for loop for each character in the punctuation list
    for char in punctuation:
        #replacing each punctuation mark found in the line with nothing
        current_line = current_line.replace(char, "")

    #.upper function so words in line can be compatible with words from database
    current_line = current_line.upper()
    ordered_word_list = current_line.split(" ")
    return ordered_word_list

print(remove_punctuation("Hang, cur! hang, you whoreson, insolent noisemaker!"))