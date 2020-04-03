#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Vesna
#
# Created:     26.03.2020
# Copyright:   (c) Vesna 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Balon(object):

    jedinstvene_boje = set()

    def __init__(self, boja):
        self.boja = boja
        Balon.jedinstvene_boje.add(boja)

    @staticmethod
    def brojJedinstvenihBoja():
        return len(Balon.jedinstvene_boje)

    def jedinstveneBoje():
        return Balon.jedinstvene_boje.copy()
    jedinstveneBoje = staticmethod(jedinstveneBoje)

b1 = Balon("plava")
b2 = Balon("crvena")
b3 = Balon("plava")

print(Balon.brojJedinstvenihBoja())
print(Balon.jedinstveneBoje())



class Duljina(object):
     konverzija = {
        'mi':621.371e-6, 'milje':621.371e-6, 'milja':621.371e-6,
        'yd':1.094,      'jard':1.094,       'jarda':1.094,      'jardi':1.094,
        'ft':3.281,      'stope':3.281,      'stopa':3.281,
        'in':39.37,      'palac':39.37,      'palca':39.37,      'palaca':39.37,
        'mm':1000,       'milimetar':1000,   'milimetara':1000,  'milimetra' : 1000,
        'cm':100,        'centimetar':100,   'centimetara':100,  'centimetra':100,
        'm':1.0,         'metar':1.0,        'metara':1.0,       'metra':1.0,
        'km':0.001,      'kilometar':0.001,  'kilometara':0.001, 'kilometra':0.001
     }

     brojevi = frozenset("0123456789.eE-+")

     def __init__(self, duljina = None):          #Duljina("32.4 milje")
          if duljina is None:
               self.__iznos=0.0
          else:
               znamenke = ""
               for i, znak in enumerate(duljina):
                    if znak in Duljina.brojevi:
                         znamenke += znak
                    else:
                         try:
                              self.__iznos = float(znamenke)
                              jedinica = duljina[i:].strip().lower()
                              self.__iznos /= Duljina.konverzija[jedinica]
                         except:
                              raise ValueError("nevaljan iznos i/ili mjerna jedinica")
                         break
               else:
                    raise ValueError("potreban je iznos i mjerna jedinica")

     def stavi(self, duljina):
          self.__init__(duljina)

     def u(self, jedinica):
          return self.__iznos * Duljina.konverzija[jedinica]

     """def copy(self):
          other = Duljina()
          other.__iznos = self.__iznos
          return other"""

     def copy(self):
          import copy
          return copy.copy(self)

     @staticmethod
     def jedinice():
          return Duljina.konverzija.keys()

     def __eq__(self, other):
          return self.__iznos == other.__iznos

     def __lt__(self, other):
          return self.__iznos < other.__iznos

     def __le__(self,other):
          return self.__iznos <= other.__iznos

     def __repr__(self):
          return "Duljina('%fm')" % self.__iznos

     def __str__(self):
          return "%.3fm" % self.__iznos

     def __add__(self, other):
          return Duljina("%fm" % (self.__iznos + other.__iznos))

     def __mul__(self, other):
          if isinstance(other, Duljina):
               raise ValueError("Duljina * Duljina daje povrsinu")
          return Duljina("%fm" % (self.__iznos * other))

     def __truediv__(self, other):
          if isinstance(other, Duljina):
               raise ValueError("Duljinu ne mozemo dijeliti s duljinom")
          return Duljina("%fm" % (self.__iznos / other))

     def __float__(self):
          return float(self.__iznos)

     def __int__(self):
          return int(round(self.__iznos))

d = Duljina("100 cm")

x = Duljina("30 ft")
y = Duljina("250 cm")
print(x)
print(y)
z = x + y
print(z)
x+=y
print(x)

a = Duljina("300 m")
b = Duljina("1 km")
