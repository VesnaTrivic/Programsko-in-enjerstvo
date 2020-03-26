#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Vesna
#
# Created:     25.03.2020
# Copyright:   (c) Vesna 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Stolica(object):
    """ Ova klasa predstavlja stolicu """

    def __init__(self, ime, broj_nogu = 4):
        self.ime = ime
        self.broj_nogu = broj_nogu

stolica1 = Stolica("Barcelona")
stolica2 = Stolica("Barska stolica", 1)

print(stolica1.ime)
print(stolica1.broj_nogu)
stolica1.broj_nogu = 2
print(stolica1.broj_nogu)



class Pravokutnik(object):

    def __init__(self, sirina, visina):
        self.sirina = sirina
        self.visina = visina

    def getSirina(self):
        return self.sirina

    def setSirina(self, value):
        self.sirina = value

    def getVisina(self):
        return self.visina

    def setVisina(self, value):
        self.visina = value

    def povrsina(self):
        return self.getSirina() * self.getVisina()

p = Pravokutnik(50,10)
print(p.povrsina())
p.setSirina(20)
print(p.povrsina())



class Pravokutnik(object):

    def __init__(self, sirina, visina):
        self._sirina = sirina
        self._visina = visina

    @property
    def sirina(self):
        return self._sirina

    @sirina.setter
    def sirina(self,value):
        self._sirina = value

    @property
    def visina(self):
        return self._visina

    @visina.setter
    def visina(self,value):
        self._visina = value

    @property
    def povrsina(self):
        return self.sirina * self.visina

p = Pravokutnik(50,10)
print(p.povrsina)
p.sirina = 20
p.visina = 30
print(p.povrsina)



class Pravokutnik(object):

    def __init__(self, sirina, visina):
        self._sirina = sirina
        self._visina = visina

    @property
    def sirina(self):
        return self._sirina

    @sirina.setter
    def sirina(self,value):
        self._sirina = value

    @property
    def visina(self):
        return self._visina

    @visina.setter
    def visina(self,value):
        self._visina = value

    @property
    def povrsina(self):
        return self.sirina * self.visina

    def __eq__(self, other):
        return self.povrsina == other.povrsina

    def __lt__(self, other):
        return self.povrsina < other.povrsina

    def __le__(self, other):
        return self.povrsina <= other.povrsina

    def __repr__(self):
        return"Pravokutnik("+repr(self._sirina) + ',' + repr(self._visina) + ")"

    def __str__(self):
        return 'Pravokutnik ' + str(self._sirina) + 'x' + str(self._visina)

    def __float__(self):
        return float(self.povrsina)

    def __add__(self, other):
        return Pravokutnik(self.sirina + other.sirina, self.visina + other.visina)

p1 = Pravokutnik(3,10)
p2 = Pravokutnik(10,3)
p3 = Pravokutnik(4,20)
print(p1 == p2)
print(p1 != p2)
print(p1 < p2)
print(p3 >= p1)

p4=eval(repr(p1))
print(p1,p4)

p5 = Pravokutnik(3,4)
p6 = Pravokutnik(2,5)
p7 = p5 + p6
print(p7)