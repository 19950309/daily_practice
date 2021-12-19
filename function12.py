#!/usr/bin/python3
# vim: set fileencoding = utf-8

def hello_name():
    print('good morning')

def great(name):
    print('good morning %s' %(name))

def describe_animal(name,age=6):
    return list(['name',age])

if __name__=='__main__':
    hello_name()
    great('bob')
    a=describe_animal('dog')
    print(a)
