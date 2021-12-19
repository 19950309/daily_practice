#!/usr/bin/python3
# vim: set fileencoding = utf-8

def read_file(file_name):
    with open(file_name,'r') as file_object:
        content = file_object.read()
        print(content)


__name__ == '__main__':
    read_file('coding.txt')

