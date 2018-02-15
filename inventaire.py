import re


def inventaire(path):
    n = 1
    with open(path, 'r') as file:
        number = re.compile(r'-?[1-9][0-9]*')
        line = file.readlines()
        for i in line:
            if number.match(str(i)) is not None:
                print('line {}: {}'.format(n,i))
            n += 1

inventaire('inventaire_test.txt')