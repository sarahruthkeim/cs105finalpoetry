def word_character_list() -> None:
    file_handle = open('cmudict.txt', 'r')
    line_count = 0
    for line in file_handle:
        line_count += 1
        modified_line = ""
        for char in range(len(line[:-1])):
            if line[char] + line[char + 1] != "  ":
                modified_line += line[char]
        word_list = modified_line.split(" ")
        print(word_list)
        if line_count > 200:
            return


word_character_list()

