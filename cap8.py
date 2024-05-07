import time

global name 
global result 

def spell_name():
    for c in name:
        print(c)

name = "karen"
spell_name()

def current_time():
    global t
    t = time.time()


current_time()
print(t)

# retornando multiples valores

def days_of_week():
    return ("monday","tuesday", "wednesday","thursday","friday","saturday","sunday")



from collections import namedtuple

def person_builder():
    Person = namedtuple('Person',['name','age'])
    return Person(name='Lily', age=23)

person = person_builder()
print(person.name)