#! /usr/bin/python3
# vim: set fileencoding = utf-8

def animals(dog, cat, tigger):
    print('%d'%dog + ", "+cat+", "+tigger)
    print('dog:%d; cat:%s; tigger:%s' %(dog,cat,tigger))
if __name__ == '__main__':
  #  pass
  dog = 3
  cat='jumao'
  tigger = 'laohu'
  animals(dog,cat,tigger)
