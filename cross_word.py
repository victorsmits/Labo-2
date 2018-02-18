import re

linesregex = ['\d', '[a-z]', '[A-Z]']
columnsregex = ['[1-9]', '\d+', '[a-z]']
answer_line = ['1bc', 'bcd', 'CDE']


def checkregexcrossword(linesregex, columnsregex, answer):
    assert (len(linesregex) == len(answer))
    n = 0
    x = 0
    while n < len(answer):
        for regex_lines in linesregex:
            pattern_lines = re.compile(regex_lines)
            state_line = pattern_lines.match(answer[n]) is not None
            # print(state_line)
        n += 1

    while x < len(columnsregex):
        pattern_col = re.compile(columnsregex[x])
        for letter in answer[x]:
            state_col = pattern_col.match(letter) is not None
            print(pattern_col, letter, state_col)
        x += 1


checkregexcrossword(linesregex, columnsregex, answer_line)
