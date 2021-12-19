#!/usr/bin/python3
#vim: set fileencoding = utf-8

def describe_student(name,age=18):
    print('the student name is %s whose age is %d' % (name,age))

if __name__ == '__main__':
    describe_student('bob')
    describe_student('james',16)
    describe_student(age = 27,name='jack')
