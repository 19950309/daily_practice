#!/usr/bin/python3
# vim = set fileencoding = utf-8

def read_file(file_name):
    with open(file_name, 'r') as file_object:
        for line in file_object:
            print(line)




if __name__ == '__main__':
    read_file('coding.txt')
