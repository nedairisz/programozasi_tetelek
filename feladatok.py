import random
import math

'''
Írj eljárást, mely paraméterében kap két egész számot. 
Ezen két egész szám közötti páros számok összegét számolja ki az eljárás.

def paros1(min:int, max:int):
    i=min
    osszeg:int = 0
    while i<=max:
        if i%2==0:
            print(i)
            osszeg+=1
        i+=1
        #elágazás vége
    #ciklus vége
    print(f"A páros számok összege: {osszeg}")
    return osszeg
    '''

def paros2(min:int, max:int):
    #i=min
    osszeg:int = 0
    for i in range(min, max, 1):
        if i%2==0:
            print(i)
            osszeg+=1
        #i+=1
    print(f"A páros számok összege: {osszeg}")
    return osszeg

'''
Írj függvényt, amely generál 20 db véletlen számot -10 és 10 között.
Számold meg hány negatív szám van közötte.
A visszatérési érték a negatív számok száma
'''
'''
def negativ1():
    i:int = 0
    db:int=0
    while i<20:
        szam:int = math.floor(random.random()*21-10)
        print(szam)
        if szam<0:
            db+=1
        i+=1
    return db
'''

def negativ2():
    #i:int =0
    db:int=0
    for i in range(0,20,1):
        szam:int = math.floor(random.random()*21-10)
        print(szam)
        if szam<0:
            db+=1
        #i+=1
    return 

#Írj függvényt, ami generál 10 db véletlen számot 12 és 33 között és visszatér ezek összegével
def veletlen():
    vel_osszeg:int =0
    for i in range(0,10,1):
        szam:int = math.floor(random.random()*(34-12)+12)
        vel_osszeg+=szam
    return vel_osszeg

# Írj függvényt, amely generál 8db véletlen számot [20, 50) intervallumban és visszatér ezek közül a legnagyobb számmal.
def feladat1():
    max:int =0
    for i in range(0,8,1):
        szam:int = math.floor(random.random()*(50-20)+20)
        if szam>max:
            max=szam
    return max

# Kérjünk be 3db egész számokat a felhasználótól. 
# mekkora a számok átlaga?

def atlag():
    gyujto:int =0
    for i in range(0,3,1):
        szam:int= int(input(f"Kérem az {i+1}. egész számot!: "))
        gyujto+=szam
    return gyujto/3

# Kérkünk be egész számokat a felhasználótól, amyg 0 nem ad. Írjuk ki a számok átlagát.
def feladat2():
    i:int=0
    gyujto:int=0
    szamlalo:int = 1
    szam:int = int(input(f"Kérem az {i+1}. egész számot!: "))
    while szam!=0:
        szam:int = int(input(f"Kérem az {i+1}. egész számot!: "))
        gyujto+=szam
        szamlalo+=1
        i+=1
    return gyujto/(szamlalo-1)



