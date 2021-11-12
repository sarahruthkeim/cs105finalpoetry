def word_character_list() -> None:
    file_handle = open('cmudict.txt', 'r')
    for line in file_handle:
        current_line = line[:-1]
        modified_line = current_line.replace("  ", " ")
        word_list = modified_line.split(" ")
        print(word_list)





word_character_list()

