def remove_punctuation(current_line) -> list:
    """

    :return: This function checks to see if a line is iambic pentameter or not
    """
    punctuation = [":", ";", '"', "(", ")", "!", ".", "?", "", ","]
    for char in punctuation:
        current_line = current_line.replace(char, "")
    current_line = current_line.upper()
    ordered_word_list = current_line.split(" ")
    return ordered_word_list

print(remove_punctuation("Hang, cur! hang, you whoreson, insolent noisemaker!"))