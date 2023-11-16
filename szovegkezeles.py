# I.	Kérjünk be egy szöveget és végezzük el rajta a következő műveleteket, 
# majd minden végeredmény jelenítsünk meg a képernyőn még akkor is, ha ezt a feladat külön nem írja! (konzolos feladat)

# 1.    Írj metódust, mely a paraméterében kapegy szöveget: Számoljuk meg hány szóköz van a szövegben!
def feladatA(szoveg:str):
    i:int = 0
    szamlalo: int = 0
    while i<len(szoveg):
        if szoveg[i]== ' ':
            szamlalo +=1
        i +=1
    return szamlalo

# 2.	Írj metódust, mely a paraméterében kapegy szöveget: Írjuk ki a szöveget a képernyőre szóközök nélkül. 
# A továbbiakban ezzel a szöveggel dolgozzunk!
def feladatB(szoveg:str):
    i: int =0
    ujszoveg: str = ""
    while i<len(szoveg):
        if not(szoveg[i]== " "):
            ujszoveg+=szoveg[i]
        i +=1
    return ujszoveg

# 3.	Írj metódust, mely a paraméterében kapegy szöveget: Alakítsuk a szöveget kisbetűssé! A továbbiakkal ezzel a szöveggel dolgozzunk!
def feladatC(szoveg:str):
    szoveg=szoveg.lower()
    szoveg=szoveg.replace("é","e")
    szoveg=szoveg.replace("á","a")
    szoveg=szoveg.replace("ó","o")
    szoveg=szoveg.replace("ő","o")
    szoveg=szoveg.replace("ö","o")
    szoveg=szoveg.replace("ü","u")
    szoveg=szoveg.replace("ű","u")
    szoveg=szoveg.replace("í","i")
    print(szoveg.lower)
    