
# coding: utf-8

# In[1]:


print('Hello World!')


# In[1]:


for i in range(2):
    print('Hello World')


# In[2]:


# SS3 -------------

print('q')
print('b')
print('c')

x = 10
if x < 10:
    print('<10')
else:
    print('not <10')

if x <= 10:
    print('<=10')
elif x > 10 and x <= 25:
    print('10<x<=25')
elif x >= 25:
    print('x>=25')
else:
    print('Error')

y = 60
print(x%y)

print(x//y)

age = 15
if age == 15:
    print('15')
else:
    print('not 15')


# In[10]:


# SS4 --------------

'''
print a*b
:param a: int.
:param b: int.
:return: float, div a by b
'''
try:
    a = int(input('type a number'))
    b = int(input('type another'))
    print(a/b)
except (ZeroDivisionError, ValueError):
    print('invalid number')
except:
    print('unknown error')


# In[24]:


def acumulation(x):
    '''
    x**2
    :param x: int.
    :param x2: int.
    :return: int, x**2
    '''
    try:
        x = int(x)
        x2 = x**2
        return x2
    except:
        print('Error')

def printstr(x):
    '''
    Conver x into str
    :param x: str.
    :return: x as str.
    '''
    try:
        x = str(x)
        return x
    except:
        print('Error')

def acumulation2(x, pwr, IsPositivex=False):
    '''
    x**pwr, can be used only when x is a positive number.
    :param x: int.
    :param pwr: int.
    :param IsPositivex: bool.
    :return: int.
    '''
    try:
        x, pwr = int(x), int(pwr)
        if IsPositivex == True:
            if x > 0:
                return x**pwr
            else:
                print('input a positive number; IsPositivex=True')
        else:
            return x**pwr
    except:
        print('Error')

def acumulation3(x):
    '''
    x**2 // 2
    :param x: int.
    :param x2: int.
    :retrun: float.
    '''
    try:
        x2 = acumulation(x)
        return x2//2
    except:
        print('Error')

def StrToFloat(x):
    '''
    Convet x as str into x as float.
    :param x: str
    :param x2: float
    :return: float
    '''
    try:
        x = str(x)
        try:
            x2 = float(x)
            return x2
        except:
            print('could not convert it into float')
    except:
        print('it should not be a string')


x_input = input('input something')
pwr_input = input('input pwr')
str_input = input('input str')

acumulation(x_input)
print(printstr(x_input))
print(acumulation2(x_input, pwr_input))
print(acumulation2(x_input, pwr_input, IsPositivex=True))
print(acumulation3(x_input))
print(StrToFloat(str_input))


# In[34]:


# SS5 -------------

lista = []
lista.append('mr a')
lista.append('ms b')
print(lista)

tuplea = (
    ('99209', '22345'),
    ('28773', '28769'),
    ('2345', '2345')
)
print(tuplea)

dicta = {
    'height': 160,
    'color': 'black',
    'occupation': 'lovelist',
    'musician': ('mr children', 'eric clapton', 'the beatles')
}

def searchdicta(x):
    if x in dicta:
        print(dicta[x])
    else:
        print('nothing found')
        
X = input('search in dicta')
searchdicta(X)

print(dicta['musician'])

print(set(dicta['occupation']))


# In[52]:


# SS6 -----------

strA = 'kamyu'
for i in range(len(strA)):
    print(strA[i])

strB = input('input1: ')
strC = input('input2: ')
print('私は{0}して、{1}した'.format(strB, strC))

strD = 'aldous Huxley was born in 1894.'
print(strD.capitalize())

strE = 'aa?bbb?c?'
strE_splitted = strE.split('?')
print(strE_splitted[0:(len(strE_splitted)-1)])

listA = ['The', 'fox', 'was', 'born', '.']
listA_joined = ' '.join(listA)
print(listA_joined.replace(' .','.'))

strF = 'A screaming comeGs across the sky.'
print(strF.replace('s','$'))

strG = 'Hemingway'
print(strG.index('m'))

strH = 'aa \'bbb\' cc'
print(strH)

strI = ['three','three','three']
print(' '.join(strI))
print('*'.join(strI))

strJ = '4月の晴れた寒い日で、時計がどれも十三時を打っていた。'
print(strJ[0:strJ.index('、')])


# In[72]:


tv = ['GOT', 'Narcos', 'Vice']
tv2 = tv.copy()

i = 0
for j in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i += 1

print(tv)

for i, new in enumerate(tv2):
    new = tv2[i]
    new = new.upper()
    tv2[i] = new

print(tv2)

strA = ['Walking dead','Ants','Sops','Vamps']
i = 0
for str in strA:
    print(i, strA[i])
    i += 1

for j in range(25,51):
    print(j)

listA = [1,2,3,4,5]
while True:
    guess = input('input an integer. q to exit.')
    if guess == 'q':
        print('exit.')
        break
    try:
        intguess = int(guess)
        if intguess in listA:
            print('bingo')
        else:
            print('not found')
    except:
        print('type integer or q')

listB = [8,19,148,4]
listC = [9,1,33,83]
listD = []
for i in listB:
    for j in listC:
        listD.append(i*j)
print(listD)


# In[80]:


# SS8 -------------
import statistics as st
import cubed as cu   # originally created

intA = [1,5,44,66,3,78,43]
print(st.stdev(intA))

print(cu.cube(1.5))


# In[77]:


# cubed.py

def cube(x):
    '''
    return x**3
    :param x: numeric
    :param x2: numeric
    :return: numeric
    '''
    try:
        x2 = x**3
        return x2
    except:
        print('error')


# In[81]:


# SS9 -------------
import os

print(os.getcwd())
st = open('testSS9.txt','w')
st.write('Say something')
st.close()


# In[82]:


with open('test2-SS9.txt','w') as textoutfile:
    textoutfile.write('Say hello')


# In[85]:


listA = []
with open('test2-SS9.txt','r',encoding='utf-8') as readfile:
    listA.append(readfile.read())

print(listA)


# In[88]:


import csv
with open('testcsv.csv','w',newline='') as f:
    w = csv.writer(f,delimiter=',')
    w.writerow(['one',2,'three'])
    w.writerow(['atir',True,'six'])

with open('testcsv.csv','r') as f:
    r = csv.reader(f,delimiter=',')
    for row in r:
        print(' '.join(row))


# In[98]:


import os
import csv

with open('test2-SS9.txt', 'r') as f:
    r = f.read()
    for letter in r:
        print(' '.join(letter))
        
def inquery():
    inq = input('type something')
    return inq

Inq = inquery()
with open('inquerywrite-SS9.txt','w') as f:
    f.write(Inq)

with open('inquerywrite-SS9.txt','r') as f:
    print(f.read())

listA = [
    ['トップガン', 'Risky Business', 'Minority Report'],
    ['Titanic', 'The Revenant', 'Inception'],
    ['Training Day', 'Man on Fire', 'フライト']
]

with open('csvwritetest-SS9.csv','w', newline='', encoding='utf-8') as f:
    w = csv.writer(f, delimiter=',')
    for row in range(len(listA)):
        w.writerow(listA[row])

with open('csvwritetest-SS9.csv', 'r', encoding='utf-8') as f:
    r = csv.reader(f, delimiter=',')
    for row in r:
        print('|'.join(row))


# In[104]:


# SS10 hangman ----------------
import random

def hangman(word):
    wrong = 0
    stages = [
        '',
        '_____     ',
        '|         ',
        '|    |    ',
        '|    o    ',
        '|   /|\   ',
        '|   / \   ',
        '|         '
    ]
    rletters = list(word)
    board = ['_'] * len(word)
    win = False
    print('hangman started.')
    
    while wrong < len(stages) - 1:
        print('\n')
        msg = 'predict a character: '
        char = input(msg)
        if char in rletters:
            c_index = rletters.index(char)
            board[c_index] = char
            rletters[c_index] = '$'
        else:
            wrong += 1
        
        print(' '.join(board))
        
        e = wrong + 1
        print('\n'.join(stages[0:e]))
        
        if '_' not in board:
            print('you won.')
            print(' '.join(board))
            win = True
            break
    
    if not win:
        print('\n'.join(stages[0:wrong+1]))
        print('you lost. the answer is {0}'.format(word))

Word = ['Ham', 'Ion', 'Good']
Num = random.randint(0,2)
hangman(Word[Num])


# In[105]:


# SS12 ---------------

class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        self.mold = 0
        print('Created.')
    
    def rot(self, days, temp):
        self.mold = days * temp

orange1 = Orange(200, 'yellow')
print(orange1.mold)
orange1.rot(20,30)
print(orange1.mold)


# In[106]:


class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w
    
    def getArea(self):
        return self.length * self.width
    
    def change_size(self, l, w):
        self.length = l
        self.width = w
        
rect1 = Rectangle(100,300)
print(rect1.getArea())
rect1.change_size(300,300)
print(rect1.getArea())


# In[113]:


import math
import numpy as np

class Apple:
    def __init__(self, s, c, t, p):
        self.scale = s
        self.color = c
        self.taste = t
        self.price = p

class Circle:
    def __init__(self, r):
        self.radius = r
    
    def culc(self):
        a = []
        a.append(self.radius*2*math.pi)
        a.append(self.radius**2*math.pi)
        return a

class Triangle:
    def __init__(self, b, h):
        self.bottom = b
        self.height = h
    
    def get_area(self):
        area = self.bottom * self.height * (1/2)
        return area
    
    def post_param(self, b, h):
        self.bottom = b
        self.height = h
        
class Hexagon:
    def __init__(self, s):
        self.side = s
    
    def get_circum(self):
        circum = self.side * 6
        return circum
    
circle1 = Circle(10)
print(np.round(circle1.culc(),2))

tri1 = Triangle(10,8)
print(tri1.get_area())

hex1 = Hexagon(9)
print(hex1.get_circum())


# In[119]:


# SS13 --------------

class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l
        
    def print_size(self):   # overrided
        print('{0} by {1}'.format(self.width, self.len))

class Square(Shape):
    def area(self):
        return self.width * self.len
    
    def print_size(self):   # overriding
        print('{0} by {1} as a square'.format(self.width, self.len))
    
squareA = Square(10,80)
print(squareA.area())
squareA.print_size()

class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner
    
class Person:
    def __init__(self, name):
        self.name = name

mick = Person('Mick Jagger')
stan = Dog('Stanley', 'Bulldog', mick)
print(stan.owner.name)


# In[135]:


class Shape:
    def __init__(self):
        pass
    
    def what_am_i(self):
        print('I am a shape')

class Rectangle(Shape):
    def __init__(self, l, w):
        self.length = l
        self.width = w
        
    def get_perimeter(self):
        return self.length*2 + self.width*2
    
class Square(Shape):
    def __init__(self, s):
        self.side = s
        
    def get_perimeter(self):
        return self.side * 4
    
    def change_size(self, s):
        self.side = self.side + s

class Horse:
    def __init__(self, horsename, owner):
        self.horsename = horsename
        self.owner = owner
        
class Rider:
    def __init__(self, humanname, age):
        self.humanname = humanname
        self.age = age
        
rect1 = Rectangle(10,90)
sqr1 = Square(50)
print(rect1.get_perimeter(), sqr1.get_perimeter())

sqr1.change_size(5)
print(sqr1.get_perimeter())
sqr1.change_size(7)
print(sqr1.get_perimeter())

shape1 = Shape()
print(shape1.what_am_i())

print(sqr1.what_am_i())

rider1 = Rider('Mr1', 45)
horse1 = Horse('uma', rider1)

print(horse1.owner.age)


# In[154]:


# SS14 --------------
import random as rnd

# class variables ----------
class Rectangle:
    rlist = []   # not recommended. 'constant numbers' are commonly used.
    
    def __init__(self, l, w):
        self.length = l
        self.width = w
        self.rlist.append((self.length, self.width))
        
    def get_size(self):
        print('{0} x {1} = (2)'.format(self.length, self,width, self.length*self.width))

r1 = Rectangle(20,30)
r2 = Rectangle(20,100)
r3 = Rectangle(50,50)

print(Rectangle.rlist)   # call the class variable

class Square:
    square_list = []
    
    def __init__(self, s):
        self.side = s
        self.square_list.append(self.side)
    
    def __repr__(self):
        return print('{0} by {0} by {0} by {0}'.format(self.side))
        
s1 = Square(5)
s2 = Square(10)
s3 = Square(15)
print(Square.square_list)

# print(s1)

def IsAandB(a, b):
    try:
        if a is b:
            return True
        else:
            return False
    except:
        print('error')

def randomAB():
    listAB = ['yes','no','undecided']
    num1, num2 = rnd.randint(0,2), rnd.randint(0,2)
    a = listAB[num1]
    b = listAB[num2]
    return a, b
    
A, B = randomAB()

print(A, B, IsAandB(A,B))


# In[170]:


# SS15 ----------------
from random import shuffle

class Card:
    '''
    Generate a card that has one suit & one value
    '''
    
    suits = ['spades','hearts','diamonds','clubs']
    values = [None,None,'2','3','4','5','6','7','8','9','10','Jach','Queen','King','Ace']
    
    def __init__(self, v, s):
        '''
        :param v: int.
        :param s: int.
        '''
        self.value = v
        self.suit = s
        
    def __lt__(self, c2):
        '''
        if self is less than the other card
        :param c2: Card instance
        :return: bool
        '''
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False
    
    def __gt__(self, c2):
        '''
        if self is greater than the other card
        :param c2: Card instance
        :return: bool
        '''
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False
    
    '''
    def __add__(self, card2):
        return self.value + card2.value
    '''

    def __repr__(self):
        '''
        return the description of a Card instance
        :return: str
        '''
        v = self.values[self.value] + ' of ' + self.suits[self.suit]
        return v

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)
    
    def rm_card(self):
        if len(self.cards) == 0:
            return   # -> return None
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name
        print(type(self.card))

class Game:
    def __init__(self):
        name1 = input('type player 1\'s name: ')
        name2 = input('type player 2\'s name: ')
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)
    
    def wins(self, winner):
        print('{0} won this round'.format(winner))
    
    def draw(self, p1n, p1c, p2n, p2c):
        print('{0} drew {1}, and {2} drew {3}.'.format(p1n, p1c, p2n, p2c))
        
    def play_game(self):
        cards = self.deck.cards
        print('start the game.')
        while len(cards) >= 2:
            msg = 'q to quit, any other keys to play.'
            response = input(msg)
            if response == 'q':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)
        
        win = self.winner(self.p1, self.p2)
        print('the game finished. {0} won.'.format(win))
    
    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return 'draw.'

game1 = Game()
game1.play_game()

