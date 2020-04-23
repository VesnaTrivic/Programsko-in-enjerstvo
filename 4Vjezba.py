'''class Klasa1(object):

     def metodaA():

class Klasa2(Klasa1):

     def metodaA():'''


class Djelo(object):

     def __init__(self, umjetnik, naziv, godina = None):
          #print("Djelo init")
          self.__umjetnik = umjetnik
          self.__naziv = naziv
          self.__godina = godina

     def umjetnik(self):
          return self.__umjetnik

     def setUmjetnik(self, umjetnik):
          self.__umjetnik = umjetnik

     def naziv(self):
          return self.__naziv

     def setNaziv(self, naziv):
          self.__naziv = naziv

     def godina(self):
          return self.__godina

     def setGodina(self, godina):
          self.__godina = godina

     def __str__(self):
          godina = ""
          if self.__godina is not None:
               godina = " %d" % self.__godina
          return "%s - %s%s" % (self.__naziv, self.__umjetnik, godina)

class Dimenzija():

     def povrsina(self):
          raise NotImplementedError("Dimenzija.povrsina()")

     def volumen(self):
          raise NotImplementedError("Dimenzija.volumen()")

class Slika(Djelo, Dimenzija):

     def __init__(self, umjetnik, naziv, godina = None, sirina = None, visina = None):
          #print("Slika init")
          Djelo.__init__(self, umjetnik, naziv, godina)
          self.__sirina = sirina
          self.__visina = visina
          #super(Slika, self).__init__(umjetnik, naziv, godina)

     def povrsina(self):
          if self.__sirina is None or self.__visina is None:
               return None
          return self.__sirina * self.__visina

     def volumen(self):
          return None

class Skulptura(Djelo):

     def __init__(self, umjetnik, naziv, godina = None, materijal = None):
          super(Skulptura, self).__init__(umjetnik, naziv, godina)
          self.__materijal = materijal

     def __str__(self):
          materijal = ""
          if self.__materijal is not None:
               materijal = " (%s)" % self.__materijal
          return "%s%s" % (super(Skulptura, self).__str__(), materijal)

class Naziv(object):

     def __init__(self, naziv):
          self.__naziv = naziv

     def naziv(self):
          return self.__naziv

'''djela = []
djela.append(Slika("Pablo Picasso", "Zena koja place", 1937))
djela.append(Skulptura("Ivan Mestrovic", "Indijanci", 1928, "bronca"))
djela.append(Naziv("Rat i mir"))

try:
     for djelo in djela:
          if hasattr(djelo, "naziv") and callable(djelo, naziv):
               print(djelo.naziv())
          #if isinstance(djelo, Djelo):
               #print(djelo.umjetnik())
except AttributeError:
     print("greska")'''

#djelo1 = Djelo("Tolstoj", "Rat i mir")
#slika1 = Slika("Leonardo da Vinci", "Mona Lisa")
'''a = Slika("Leonardo da Vinci", "Mona Lisa", 1505)
b = Skulptura("August Rodin", "The Kiss", 1889, "mramor")
print(a)
print(b)'''

c = Slika("Pablo Picasso", "Zena koja place", 1937, 100, 200)
print(c.povrsina())
print(c.volumen())