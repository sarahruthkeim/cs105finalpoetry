num_of_lines = 0
user_poem_file = open("user_poem.txt", "r")
for line in user_poem_file:
    num_of_lines += 1

def haiku() -> bool:
    """

    :return:
    """
    if num_of_lines == 3:  # preconditions (checks that the poem has 3 lines as a haiku should)
        line_count = 1
        for line in user_poem_file:
            if line_count == 1 or line_count == 3:
                if (# call syllable counter function) != 5:
                    return False
                line_count += 1
            elif line_count == 2:
                if (# call syllable counter function) != 7:
                    return False
                line_count += 1
        return True


def limerick() -> bool:
    """

    :return:
    """
