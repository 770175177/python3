#!/usr/bin/python3

class people:
    # public attribute
    name = ''
    age = 0
    # protect attribute
    __weight = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s speak: I'm %d years old" %(self.name, self.age))

# inherit
class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        # father class function
        people.__init__(self, n, a, w)
        self.grade = g

    # rewrite class function
    def speak(self):
        print("%s speak: I'm %d years old, I study in grade %d" %(self.name, self.age, self.grade))

# inherit
class speaker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("I'm %s, I'm a speaker, my topic is %s" %(self.name, self.topic))

# multiple inherit
class sample(speaker, student):
    a = ''

    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)

test = sample("Tim", 25, 80, 4, 'Python')
test.speak()
super(speaker, test).speak()
super(student, test).speak()

