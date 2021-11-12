def word_character_list():
    file_handle = open('cmudict.txt', 'r')
    list_of_lists = []
    for line in file_handle:
        current_line = line[:-1]
        modified_line = current_line.replace("  ", " ")
        list_of_lists += [modified_line.split(" ")]
    return list_of_lists

test_list = word_character_list()

def find_word(list_of_lists, user_word: str) -> list:
    for line_list in range(len(list_of_lists)):
        if list_of_lists[line_list][0] == user_word:
            return list_of_lists[line_list]

print(find_word(test_list, 'WORD'))