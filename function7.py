#!/usr/bin/python3
# vim: set fileencoding = utf-8
def animals(dog,dog_age,cat,cat_age,tigger,tigger_age=43):
    print('dog: %s, dog_age: %d \ncat: %s,cat_age: %d \ntigger: %s,tigger age: %d ' %(dog,dog_age,cat,cat_age,tigger,tigger_age))

if __name__ == '__main__':
#    pass
    dog = 'chaiquan'
    cat='jumao'
    tigger='laohu'
    dog_age = 14
    cat_age=14
    tigger_age=14
    animals(dog=dog,dog_age=dog_age,cat=cat,cat_age=cat_age,tigger=tigger,tigger_age=tigger_age)
