'''
class Person:
    weight = 0
    height = 0
    old = 0
    gender = ''
    physical_strenght = 0
    character = 0
    name = ''

    def get_weight(self):
        #print('Bobik reached 120kg of weight goal!')
        self.weight += 2

    def plus_old(self):
        self.old += int(input('Enter: do you want to add some age to Bobik2.0?'))
    def __init__(self, Name, Weight, Old):
        self.name = Name
        self.old = Old
        self.weight = Weight

person1 = Person('Bobik', 7, 12)
person2 = Person('Bobik2.0', 14, 16)
person2.plus_old()
person1.get_weight()
print(person1.name, person2.name)
print('Old:', person1.old, person2.old)
print('weight:', person1.weight, person2.weight)
'''

'''
import random
class Student:
    name = ''
    sleep = 0
    power = 0
    tired = 0
    pleasure = 0
    knowledge = 0
    money = 0
    def __init__(self, name):
        self.name = name
        self.sleep = 0
        self.power=100
        self.tired = 0
        self.pleasure = 50
        self.knowledge =0
        self.money = 50
    def lesson(self):
        self.sleep += 5
        self.power -= 5
        self.tired += 5
        self.pleasure -= 5
        self.knowledge += 10
    def fight(self):
        self.sleep += 5
        self.power -= 15
        self.tired += 10
    def playing(self):
        self.sleep += 3
        self.power -= 2
        self.tired += 2
        self.pleasure += 6
        self.money -= 10
    def working(self):
        self.sleep +=3
        self.tired += 20
        self.pleasure += 3
        self.money += 10
    def sleeping(self):
        self.sleep -=50
        self.tired -= 20
        self.pleasure += 20
        self.power += 20
student1 = Student(input('Enter your name:  '))
def stats():
    print("Ваші стати: Ім'я:",student1.name)
    print('Знання:',student1.knowledge)
    print('Виснаження:',student1.tired)
    print('Енергія:',student1.power)
    print('Щастя:',student1.pleasure)
    print('Сонливість:',student1.sleep)
    print('Гроші:',student1.money)
stats()
day = 0
def game(day):
    if day >= 30:
        if student1.knowledge >= 150:
            print(' ')
            print('ВИ ПРОГРАЛИ ВАШІ ЗНАННЯ МЕНШЕ ЗА 150 У 30 ДЕНЬ')
            
        else:
            print(' ')
            print('ТИ ПЕРЕМІГ! ТВОЇ ЗНАННЯ БІЛЬШЕ ЗА 150 У 30 ДЕНЬ!')
    else:
        day = day + 1
        print(' ')
        print('-------DAY ', day,'-------')
        a = random.randint(0,1)
        if a == 1:
            student1.lesson()
            print(' ')
            print('Вибач був урок.. У тебе більше знань і ти втомився.(пропуск ходу)')
            input('Нажміть ЕНТЕР щоб продовжити - ')
            game(day)
        else:
            print(' ')
            choice = input('===Введіть що хочете зробити===\nW-працювати P-грати/розважатись F-битись S-спати ST-вчитись\nWI - Інформація про роботу\nPI-Інформація про розважання\nFI-Інформація про бійки')
            if choice == 'W' or choice == 'w':
                student1.working()
                print(' ')
                input('Нажміть ЕНТЕР щоб продовжити - ')
            elif choice == 'P'or choice == 'p':
                if student1.money == 0:
                    print(' ')
                    print('Недостатньо грошей!')
                    input('Нажміть ЕНТЕР щоб продовжити - ')
                else:
                    student1.playing()
                    print(' ')
                    input('Нажміть ЕНТЕР щоб продовжити - ')
            elif choice == 'F'or choice == 'f':
                if student1.power ==0:
                    print(' ')
                    print('Ти не можеш дратись, нема енергії!')
                else:
                    student1.fight()
                    print(' ')
                    input('Нажміть ЕНТЕР щоб продовжити - ')
            elif choice == 'S'or choice == 's':
                if student1.sleep == 0:
                    print(' ')
                    print('You cant sleep!')
                    input('Нажміть ЕНТЕР щоб продовжити - ')
                else:
                    student1.sleeping()
                    print(' ')
                    input('Нажміть ЕНТЕР щоб продовжити - ')
            elif choice == 'ST'or choice == 'st':
                student1.lesson()
                print(' ')
                input('Нажміть ЕНТЕР щоб продовжити - ')
            elif choice == 'WI'or choice == 'wi':
                print(' ')
                print('Робота дає 10 монет, але ти виснажуєшся і починає хилити до сну.')
                input('Нажміть ЕНТЕР щоб продовжити - ')
            elif choice == 'PI'or choice == 'pi':
                print(' ')
                print('Розваги вимагають 10 валюти, повишає твоє щастя і ти трохи втомлюєшся.')
                input('Нажміть ЕНТЕР щоб продовжити - ')
            elif choice == 'FI'or choice == 'fi':
                print(' ')
                print('Недороботана механіка. Забудь')
                input('Нажміть ЕНТЕР щоб продовжити - ')
            else:
                print(' ')
                print('Error')
                input('Нажміть ЕНТЕР щоб продовжити - ')
            if student1.pleasure <= 0:
                student1.pleasure =0
                print(' ')
                print('Щастя = 0. У тебе відчуття що ти готовий померти.. ')
                print('-20 енергія +20виснаження -20сонливість -30знань')
                student1.power -=20
                student1.tired+=20
                student1.sleep -=20
                student1.knowledge -=30
            if student1.sleep >= 100:
                student1.sleep = 100
                student1.sleeping()
                print(' ')
                print('УУФ! Ти виснажений! Час спати!*поспав* Тепер у тебе є енергія!')
            elif student1.sleep <=0:
                student1.sleep = 0
            if student1.power <=0:
                student1.power = 0
                b = random.randint(0,1)
                if b == 0:
                    student1.sleeping()
                    print(' ')
                    print('УУФ! Ти виснажений! Час спати!*поспав* Тепер у тебе є енергія!')
                else:
                    print(' ')
                    print('У тебе нема енергії. Подумай про це! Коли нема енергії ти не можеш дратися.')
            elif student1.power >=100:
                student1.power = 100
            if student1.tired >=100:
                student1.tired = 100
                print(' ')
                c=input('Ти виснажений. Хочеш спати чи вчитись? Введіть: sl-спати/st-вчитись')
                if c=='sl'or choice == 'SL':
                    student1.sleeping()
                    print(' ')
                    print('Солодких снів :)')
                elif c == 'st'or choice == 'ST':
                    student1.lesson()
                    print(' ')
                    print('Ти добре попрацював.. ой.. +15 знань. щастя=1')
                    student1.knowledge +=5
                    student1.pleasure = 1
            elif student1.tired <=0:
                student1.tired = 0
            if student1.money <=0:
                student1.money = 0
                student1.working()
                print(' ')
                print('Тобі потрібно йти на роботу. Утебе нема грошей!')
            elif student1.money >=100:
                student1.money = 100
        stats()
        game(day)
game(day)
'''
'''
class Car:

    def __init__(self,model,speed,weight,):
        self.speed = speed
        self.model = model
        self.weight = weight
        self.passangers=[]
    def add_passanger(self, passanger):
        self.passangers.append(passanger)
    def show(self):
        for i in self.passangers:
            print(i.name)
class Person:
    def __init__(self, name,old):
        self.name = name
        self.old = old
you = Person(input('Enter your name: '), int(input('Enter your age: ')))
bon= Person('Bon', 55)
car1 = Car(input('Enter model of car: '), float(input('Enter max speed of car: ')),float(input('Enter the weight of car: ')))
car1.add_passanger(you)
car1.add_passanger(bon)
car1.show()
'''
'''
import random
class Home:
    def __init__(self, area):
        self.mebel = []
        self.people = []
        self.area = area
class Car:

    def __init__(self,model,speed,weight,cprice):
        self.speed = speed
        self.model = model
        self.weight = weight
        self.new = 0
        self.cprice=cprice
class Job:
    def __init__(self, salary, name):
        self.salary = salary
        self.name = name
class Place:
    def __init__(self, country, town):
        self.country = country
        self.town = town
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.happiness = 100
        self.tired = 0
        self.money = 0
        self.car = None
        self.job = None
        self.home = None
    def buy_car(self, money, cprice, car):
        if money >= cprice:
            self.car = car
            print('you got a car')
        else:
            print('not enought money')
            print('not enought money')
    def buy_home(self, money, hprice, home):
        if money >= hprice:
            self.home = home
            print('you got a car')
        else:
            print('not enought money')
    def get_job(self, job):
        a= random.randint(0,1)
        if a==1:
            self.job = job
            print('you got a job')
    def work(self, salary):
        self.happiness -= 10
        self.tired += 10
        self.money +=salary

'''
'''
class Person:
    def __init__(self,name,age,money):
        self.name=name
        self.tired = 0
        self.happy = 100
        self.age = age
        self.money = money
class Student(Person):

    def __init__(self):
        super().__init__()
        self.freetime = 0 # <----- :(
        self.know = 0
    def relax(self):
        self.tired-=10
        self.happy += 10
student1 = Student('bob',14,10)
student2 = Student('boob',15,30)

print('-- ',student1.tired, student1.happy)
print('-- ',student2.tired, student2.happy)
'''
'''
class Square():
    def __init__(self, side):
        self.side = side
    def area(self):
        self.area = self.side **2
        print('Area of square that has side ', self.side, 'sm = ', self.area,'sm2')
square1=Square(2)
square1.area()
class Paralelogram(Square):
    def __init__(self, side, side2):
        super().__init__(side)
        self.side2 = side2
    def area2(self):
        self.area2 = self.side * self.side2
        print('Area of Paralelogram that has sides ', self.side,'sm and 2nd side',self.side2, 'sm = ', self.area2,'sm2')
paralelogram1 = Paralelogram(3,5)
paralelogram1.area2()
'''
'''
class Soda:
    def __init__(self, v, add=None):
        self.add = add
        self.v = v
    def my_drink(self):
        if self.add == None:
            print('Lemonade ', self.add, 'ml')
            print('No additives')
        else:
            print('Lemonade ', self.add, 'ml')
            print('Additive:', self.v)
drink1=Soda(int(input('How much lemonade do you want?(ml): ')), input('What do you want to add?(press Enter if nothing): '))
drink1.my_drink()
'''
'''
class InvalidTriangle(Exception):
    def __str__(self):
        return 'Stop doing triangles like that!'
class TriangleCheck:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def is_it(self):
        if self.side1 <=0 or self.side2 <=0 or self.side3 <=0 or type(self.side1 or self.side2 or self.side3) != int :
            raise InvalidTriangle()
        else:
            print('We can make triangle!')
try:
    triangle = TriangleCheck(int(input('Side 1 = ')), int(input('Side 2 = ')), int(input('Side 3 = ')))
    triangle.is_it()
except ValueError:
    raise InvalidTriangle()
else:
    pass
'''


'''
try:
    a = int(input('How old are you?'))
except ValueError:
    print('Value Error!')
else:
    if a <=17:
        print('Sorry, we cant let you ride a bike.')
    else:
        print('There is your bike!')
'''
'''
def lol():
    raise TypeError('Sorry, invalid tax') 
lol()
'''
'''
a = int(input('Enter number a : '))
b = int(input('Enter number b: '))

result = [a/b]
class Divider:
    def divider():
        if a < b:
            raise ValueError('Number b can not be > than number a')
        if b > 100:
            raise IndexError('b cant be bigger than 100')
        return a/b
try:
    data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4}

    for key in data:
        res = Divider.divider(key, data[key])
        result.append(res)
except:
    Divider.divider()
finally:
    print(result)
'''
'''
print('hello world')
a= 1
b=2
c=3
print(a+b+c)
print(a-b-c)
'''
'''
def ex():
    print('Ex1')
    print('Латунний циліндр масою 1kг і температурою 100С опустили у воду 10С масою 300г. Знайти температуру води і циліндра після зрівняння температур(t)')
    print('Дано:')
    m1=float(input('m1(маса циліндра) = '))
    m2=float(input('m2(маса води) = '))
    c2=float(input('c2(питома теплоємність води) = '))
    c1=float(input('c1(питома теплоємність латуні) = '))
    t1 = float(input('to1= '))
    t2 = float(input('to2= '))
    print('t-?')
    print('           ')
    print('Q1- = Q2+')
    print('c1m1(to1-t)=c2m2(t-to2)')
    print('c1m1to1-c1m1t=c2m2t-c2m2to2')
    print('c1m1to1+c2m2to2=c2m2t+c1m1t')
    print('c1m1to1+c2m2to2=t(c2m2+c1m1)')
    print('t=(c1m1to1+c2m2to2)/(c1m1+c2m2)')
    t = (c1*m1*t1+c2*m2*t2)/(c1*m1+c2*m2)
    print('Your t =',t,'C Correct t = 31.686746987951807 C')
ex()
'''
'''
for i in range(15):
    print('hello world')
'''
'''
import requests
from bs4 import BeautifulSoup as bs


#grn = int(input('Enter grn: '))
r = requests.get("https://auto.ria.com/uk/legkovie/lamborghini/?page=1")
html = bs(r.text, "html.parser")
data = html.find_all('div', class_= 'price-ticket')
cur = []
data2 = html.find_all('div', class_= 'adress')
cur2 = []
for i in data2:
    print(i.span.text)
for i in data:
    print(i.span.text)


#print(f'EUR: {grn / cur[0]}\nUSD: {grn / cur[1]}\nPLN: {grn / cur[2]}')
'''
'''
import requests
from bs4 import BeautifulSoup as bs


#grn = int(input('Enter grn: '))
r = requests.get("https://meteo.ua/ua/34/kiev#2023-11-17--19-00")
html = bs(r.text, "html.parser")
day = html.find_all('div', class_= 'menu-basic__day' )
cur = []
day2 = html.find_all('div', class_= 'menu-basic__month')
cur2 = []
daytem = html.find_all('div', class_= 'menu-basic__degree')
cur3 =[]
for i in day:
    cur.append(i.text)
for i in day2:
    cur2.append(i.text)
for i in daytem:
    cur3.append(i.text)
for i in range(len(cur)):
    print(cur[i], cur2[i], cur3[i])
'''


#print(f'EUR: {grn / cur[0]}\nUSD: {grn / cur[1]}\nPLN: {grn / cur[2]}')

'''

import sqlite3


conection = sqlite3.connect('shop.db')
cursor = conection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, 
               name VARCHAR(100) UNIQUE NOT NULL,
               password VARCHAR(100) NOT NULL);""")

conection.commit()
conection.close()
# conection = sqlite3.connect('shop.db')
# cursor = conection.cursor()
# cursor.execute("""INSERT INTO user(name, password) VALUES ('Bob', '12354'), ('Jack', 'wasd');""")
# conection.commit()
# conection.close()

conection = sqlite3.connect('shop.db')
cursor = conection.cursor()
cursor.execute("""SELECT * FROM user; """)
data = cursor.fetchall()
print(data)
conection.close()
'''
'''
import sqlite3


conection = sqlite3.connect('film1.db')
cursor = conection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS film (id INTEGER PRIMARY KEY, 
                name VARCHAR(100) UNIQUE NOT NULL,
                year DATE NOT NULL),
                janre VARCHAR(100) NOT NULL,
                reg VARCHAR(100) NOT NULL;""")
cursor.execute("""CREATE TABLE IF NOT EXISTS regiser (id INTEGER PRIMARY KEY, 
                name VARCHAR(100) UNIQUE NOT NULL,
                year DATE NOT NULL);""")


conection = sqlite3.connect('film1.db')
cursor = conection.cursor()
cursor.execute("""INSERT INTO film(name, year, janre, reg) VALUES ('Iron Man', '2008-01-12', 'Superhero film', 'John Favro'), 
               ('Iron Man 2', '2010-12-05', 'Superhero film', 'John Favro'),
               ('Tor love & thunder', '2022-05-07', 'Superhero film', 'Taika Vaity'),
               ('On western front without changes', '2022-08-12', 'Action', 'Eduart Berger');""")
cursor.execute("""INSERT INTO regiser(name, year) VALUES ('John Favro', '1966-09-10'), ('Taika Vaity', '1975-08-06'), ('Eduart Berger', '1970-09-01');""")


conection = sqlite3.connect('film1.db')
cursor = conection.cursor()
cursor.execute("""SELECT * FROM film WHERE janre = Superhero film; """)
cursor.execute("""SELECT * FROM regiser; """)
data = cursor.fetchall()
print(data)
conection.close()
'''
'''
import cv2
image_path = 'cat1.jpg'
image = cv2.imread(image_path)
cv2.imshow('Cat', image)
cv2.waitKey()
'''
'''
import cv2
image_path = 'cat1.jpg'
cat_face_cascade = cv2.CascadeClassifier('lox.xml')
image = cv2.imread(image_path)
cat_face = cat_face_cascade.detectMultiScale(image)
print(cat_face)
for (x, y, w, h) in cat_face:
    cv2.rectangle(image, (x,y), (x+w, y+h), (0, 0, 255),3)
cv2.imshow('Cat', image)
cv2.waitKey()
'''
