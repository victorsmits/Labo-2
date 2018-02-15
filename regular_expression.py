import re


def match_phone_number(nmb):
    patterne = r'^\+[0-9]{2}\ [0-9]{3}\ [0-9]{2}\ [0-9]{2}\ [0-9]{2}$'
    p = re.compile(patterne)
    if p.match(nmb):
        return print(True)
    return print(False)


nmb = input('entrez numéro')
match_phone_number(nmb)


def full_number(num):
    number = r'-?[1-9][0-9]*$'
    x = re.compile(number)
    if x.match(num):
        return print(True)
    return print(False)


num = input('entrez nombre entier')
full_number(num)


def car_plate(car):
    plate = re.compile(r'[1-9][a-z]{3}[0-9]{3}$|[1-9][0-9]{3}[a-z]{3}$')
    return print(plate.match(car) is not None)


car = input('entrez numéro de plaque')
car_plate(car)


def dd_name(dd):
    disque = re.compile(r'c:\\[A-Z]+$')
    return print(disque.match(dd) is not None)


dd = input('entrez nom du disque')
dd_name(dd)
