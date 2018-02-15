import re
import sys


def inventaire(path):
    n = 1
    finde=''
    with open(path, 'r') as file:
        number = re.compile(r'\d+')
        line = file.readlines()
        for i in line:
            content = number.findall(i)
            if len(content) != 0:
                for txt in content:
                    if len(content) >1:
                        finde += '{}, '.format(txt)
                    else:
                        finde += '{}'.format(txt)
                print('line {}: {}'.format(n, finde))
                finde = ''
            n += 1

def path():
    file = re.compile(r'-[a-z]*\.txt$')
    sys = sys.arg
    for i in sys:
        if file.match(i) is not None:
            return i
#txt = path()
#inventaire(txt)
inventaire('inventaire_test.txt')