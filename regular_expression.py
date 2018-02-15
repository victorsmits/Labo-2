import re


def match_phone_number(nmb):
    patterne = r'^\+[0-9]{2}\ [0-9]{3}\ [0-9]{2}\ [0-9]{2}\ [0-9]{2}$'
    p = re.compile(patterne)
    if p.match(nmb):
        return print(True)
    return print(False)

def full_number(num):
    number = r'-?[1-9][0-9]*$'
    x = re.compile(number)
    if x.match(num):
        return True
    return False

def car_plate(car):
    plate = re.compile(r'[1-9][a-z]{3}[0-9]{3}$|[1-9][0-9]{3}[a-z]{3}$')
    return print(plate.match(car) is not None)


def dd_name(dd):
    disque = re.compile(r'c:\\[A-Z]+$')
    return print(disque.match(dd) is not None)



if __name__ == '__main__':
    nmb = input('entrez numéro')
    match_phone_number(nmb)

    num = input('entrez nombre entier')
    print(full_number(num))

    car = input('entrez numéro de plaque')
    car_plate(car)

    dd = input('entrez nom du disque')
    dd_name(dd)