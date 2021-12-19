#!/usr/bin/python3
# vim: set fileencoding = utf-8

def describe_student(name,age=18):
 #   return('the student name is %s whose age is %d' % (name, age))
     
    #return {name:age}
    return dict({name:age})

if __name__=='__main__':
    print(describe_student('bob'))
    b=describe_student('james',16)
    c=describe_student(age=27, name = 'jack')
    print('%s \n%s' %(b,c))
