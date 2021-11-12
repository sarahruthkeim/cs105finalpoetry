def word_character_list() -> None:
    file_handle = open('cmudict.txt', 'r')
    for line in file_handle:
        modified_line = ""
        for char in range(len(line[:-1])):
            if line[char] + line[char + 1] != "  ":
                modified_line += line[char]
        word_list = modified_line.split(" ")



word_character_list()

