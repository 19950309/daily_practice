#!/usr/bin/python3
# vim: set fileencoding = utf-8



def open_api(filename):
    with open(filename, 'w') as file_object:
        file_object.write('I Love programming')
        file_object.write('\nKingstar boyue')

if __name__ == '__main__':
    filename = 'coding.txt'
    open_api(filename)
