import os, re

class FilePath:
    FILE = 'integerArray.txt'


def read_file(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_input(filename):
    lines = read_file(filename)
    lines = map(lambda s: re.sub('\s+', ' ', str(s.strip('\r\n'))).strip(), lines)
    return lines
