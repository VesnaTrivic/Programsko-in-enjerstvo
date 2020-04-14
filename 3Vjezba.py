rj = {"a": "alfa", "b": "beta", "o": "omega"}

'''print(rj)
for k,v in rj.items():
     print(k,v)'''

import bisect

class UredjeniRjecnik(object):
     def __init__(self, rjecnik = None):
          self.__kljucevi = []
          self.__rjecnik = ()

          if rjecnik is not None:
               if isinstance(rjecnik, UredjeniRjecnik):
                    self.__rjecnik = rjecnik.__rjecnik.copy()
                    self.__kljucevi = list(self.__kljucevi)
               else:
                    self.__rjecnik = dict(rjecnik)
                    self.__kljucevi = sorted(self.__rjecnik.keys())

     def getAt(self, index):
          return self.__rjecnik[self.__kljucevi[index]]

     def setAt(self, index, value):
          self.__rjecnik[self.__kljucevi[index]] = value

     def __getitem__(self, key):
          return self.__rjecnik[key]

     def __setitem__(self, key, value):
          if key not in self.__rjecnik:
               bisect.insort_left(self.__kljucevi, key)
          self.__rjecnik[key] = value

     def __delitem__(self, key):
          i = bisect.bisect_left(self.__kljucevi, key)
          del self.__kljucevi[i]
          del self.__rjecnik[key]

     def get(self, key, value = None):
          return self.__rjecnik.get(key, value)

     def setdefault(self, key, value):
          if key not in self.__rjecnik:
               bisect.insort_left(self.__kljucevi, key)
          return self.__rjecnik.setdefault(key, value)

     def popitem(self):
          item = self.__rjecnik.popitem()
          i = bisect.bisect_left(self._kljucevi, item[0])
          del self._kljucevi[i]
          return item

     def __contains__(self, key):
          return key in self.__rjecnik

     def __len__(self):
          return len(self.__rjecnik)

     def keys(self):
          return self.__kljucevi[:]

     def values(self):
          return [self.__rjecnik[key] for key in self.__kljucevi]

     def items(self):
          return [(key, self.__rjecnik[key]) for key in self.__kljucevi]

     def __iter__(self):
          return iter(self.__kljucevi)

     def copy(self):
          rjecnik = UredjeniRjecnik()
          rjecnik.__kljucevi = list(self.__kljucevi)
          rjecnik.__rjecnik = dict(self.__rjecnik)
          return rjecnik

     def clear(self):
          self.__kljucevi = []
          self.__rjecnik = ()

     def __repr__(self):
          djelovi = []
          for key in self.__kljucevi:
               djelovi.append("%r : %r" % (key, self.__rjecnik[key]))
          return "UredjeniRjecnik((" + ", ".join(djelovi) + "))"

     def __str__(self):
          return repr(self)

'''urj = UredjeniRjecnik(rj)
print(urj.getAt(0))
print(urj.getAt(1))
print(urj.getAt(2))'''

urj = UredjeniRjecnik(rj)

for el in urj:
     print(el)


d = UredjeniRjecnik({'s' :1, 'a' :2, 'n' :3, 'i' :4, 't':5})
print(repr(d))
d = UredjeniRjecnik({2: 'a', 3: 'm', 1: 'x'})
print(d)