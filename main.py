import feladatok


eredmeny:int = feladatok.paros(20, 52)

#Írj függvényt, amely generál 20 db véletlen számot -10 és 10 között.
#Számold meg hány negatív szám van közötte.
#A visszatérési érték a negatív számok száma

negativ_db:int = feladatok.negativ()
print(f"A negatív számok száma: {negativ_db}")

#Írj függvényt, ami generál 10 db véletlen számot 12 és 33 között és visszatér ezek összegével

vel_osszeg:int = feladatok.veletlen()
print(f"A véletlen számok összege: {vel_osszeg}")

feladatok.feladat1()
feladatok.atlag()
feladatok.feladat2()

feladatok.veletlen2()
feladatok.atlag2()
feladatok.feladat1While()