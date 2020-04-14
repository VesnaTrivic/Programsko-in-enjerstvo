class MultiSkup(object):
     def __init__(self, kljucevi):
          self.__kljucevi = kljucevi
          self.__rjecnik = {}

     def __str__(self):
          self.__rjecnik = {}
          for l in self.__kljucevi:
               if self.__rjecnik.get(l):
                    vrijednost=self.__rjecnik[l]
                    vrijednost += 1
                    self.__rjecnik[l] = vrijednost
               else:
                    self.__rjecnik[l] = 1

          x = "{"
          str1 = str(self.__rjecnik)
          x += str1.replace(": ","*")
          x += "}"
          return x

     def __iter__(self):
          return iter(self.__kljucevi)

     def __repr__(self):
          return "MultiSkup" + "(" + str(self.__kljucevi) + ")"

     def add(self, kljuc, vrijednost = None):
          if vrijednost is None:
               self.__kljucevi.append(kljuc)
          else:
               for x in range(vrijednost):
                    self.__kljucevi.append(kljuc)

     def remove(self, kljuc, vrijednost = None):
          if vrijednost is None:
               self.__kljucevi.remove(kljuc)
          else:
               for x in range(vrijednost):
                    self.__kljucevi.remove(kljuc)

print('*** test 1 ***')
a = MultiSkup([1,1,2,2,2,3,3,4])
print(a)

print('*** test 2 ***')
a = MultiSkup([1,1,2,2,2,3,3,4])
for el in a:
     print(el)
print(repr(a))

print('*** test 3 ***')
a = MultiSkup([1,1,2,2,2,3,3,4])
a.add(4)
print(a)
a.add(2,3)
print(a)
a.remove(4,2)
print(a)