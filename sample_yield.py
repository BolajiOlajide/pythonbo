names = ["Bolaji", "Emmanuel", "Olajide"]


def read_names():
    for name in names:
        yield name


def get_names():
    for name in read_names():
        print('Reading ===> ' + name)


get_names()
