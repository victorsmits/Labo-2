import re

linesregex = ['\d', '[a-z]', '[A-Z]']
columnsregex = ['[1-9]', '\d+', '[a-z]']
answer_line = ['abc','bcd','CDE']

def checkregexcrossword(linesregex, columnsregex, answer):
    assert (len(linesregex) == len(answer))
    n=0
    while n < len(answer):
        for regex_lines in linesregex:
            pattern_lines = re.compile(regex_lines)
            state_line = pattern_lines.match(answer[n]) is not None
            print(state_line)

        for regex_col in columnsregex:
            pattern_col = re.compile(regex_col)
            state_col = pattern_col.match() is not None
        n += 1
checkregexcrossword(linesregex, columnsregex,answer_line)
