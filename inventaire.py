import re
import sys


def inventaire(path):
    number = re.compile(r'-?\d+')
    n = 1
    with open(path, 'r') as file:
        line = file.readlines()
        for i in line:
            content = number.findall(i)
            if len(content) != 0:
                print('line {}: {}'.format(n, ','.join(content)))
            n += 1

def path():
    file = re.compile(r'[a-z]*.txt|[a-z]\d*.txt')
    cmd = sys.argv
    for i in cmd:
        if file.match(i.lower()) is not None:
            return i

txt = path()
inventaire(txt)
