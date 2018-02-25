import re

linesregex = ['\d', '[a-z]', '[A-Z]']
columnsregex = ['[1-9]', '\d+', '[a-z]']
answer_line = ['1bc', 'def', 'HIJ']


def checkregexcrossword(linesregex, columnsregex, answer):
    assert (len(linesregex) == len(answer))
    x = 0
    z = 0
    col = {}
    line = {}
    while x < len(linesregex):
        y = x+1
        if y in line:
            line[y] = ''
        line[y] = answer[x]
        pattern_lines = re.compile(linesregex[x])
        state_line = pattern_lines.match(line[y]) is not None
        print('Line', linesregex[x], ':', line[y], ':', state_line)
        x += 1

    while z < len(columnsregex):
        y = z + 1
        letter_list = []
        for letter in answer:
            letter_list.append(letter[z])
        if y in col:
            col[y] = ''
        col[y] = ''.join(letter_list)
        pattern_col = re.compile(columnsregex[z])
        state_col = pattern_col.match(col[y]) is not None
        print('Column', columnsregex[z], ':', col[y], ':', state_col)
        z += 1



checkregexcrossword(linesregex, columnsregex, answer_line)
