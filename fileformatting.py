def word_character_list():
    word_list = []
    file_handle = open('cmudict.txt', 'r')
    for line in file_handle:
        modified_line = ""
        for char in range(len(line[:-1])):
            if line[char] + line[char + 1] != "  ":
                modified_line += line[char]
        broken_word_list = modified_line.split(" ")
        word_list.append(broken_word_list)
    return word_list



