import json
import sqlite3

class Ispiti(dict):

     def dodaj(self, student, kolegij, ocjena):
          if student not in self:
               self[student] = {}
          self[student][kolegij] = ocjena

     def izbrisi(self, student, kolegij):
          if kolegij in self[student]:
               self[student].pop(kolegij)

     def promijeni(self, student, kolegij, ocjena):
          self[student][kolegij] = ocjena

     def spremi_datoteka(self, datoteka):
        with open(datoteka, 'w') as d:
            studenti=self.keys()
            for i in range(len(self)):
                kolegiji=self[studenti[i]].keys()
                for j in range(len(kolegiji)):
                    ispit=studenti[i], kolegiji[j], self[studenti[i]][kolegiji[j]]
                    podaci="%s \t %s \t %s\n" %(studenti[i], kolegiji[j], self[studenti[i]][kolegiji[j]])
                    d.write(podaci)

     @staticmethod
     def ucitaj_datoteka(datoteka):
          ispit=Ispiti()
          with open(datoteka, 'r') as d:
               for i in range(len(open("ispiti.txt").readlines())):
                    line=d.readline()
                    student=(line.splitlines()[0]).split("\t")
                    ispit.dodaj(student[0],student[1],student[2])
               return ispit

     def spremi_json(self, datoteka):
        with open(datoteka, "w") as d:
            json.dump(self,d)

     @staticmethod
     def ucitaj_json(datoteka):
        with open(datoteka) as d:
            student = json.load(d)
            return student


class IspitiDB():

     def __init__(self, baza):
          self.conn = sqlite3.Connection(baza)
          self.cur = self.conn.cursor()

          self.cur.executescript("""
               DROP TABLE IF EXISTS ispiti;
               DROP TABLE IF EXISTS kolegiji;
               DROP TABLE IF EXISTS studenti;

               CREATE TABLE studenti (
               student_id integer PRIMARY KEY,
               ime_prezime text NOT NULL UNIQUE);

               CREATE TABLE kolegiji (
               kolegij_id integer PRIMARY KEY,
               naziv text NOT NULL UNIQUE);

          CREATE TABLE ispiti (
          student_id integer,
          kolegij_id integer,
          ocjena integer NOT NULL,
          PRIMARY KEY (student_id, kolegij_id),
          FOREIGN KEY (student_id) REFERENCES studenti (student_id),
          FOREIGN KEY (kolegij_id) REFERENCES kolegij (kolegij_id));
          """)

     def vrati_kolegij_id(self, naziv):
          self.cur.execute("""SELECT kolegij_id FROM kolegiji WHERE naziv = ?""", (naziv,))
          row = self.cur.fetchone()
          if row:
               return row[0]

     def dodaj_kolegij(self, naziv):
          self.cur.execute("""INSERT INTO kolegiji (naziv) VALUES (?)""", (naziv, ))
          self.conn.commit()
          return self.cur.lastrowid

     def vrati_student_id(self,ime_prezime):
        self.cur.execute("""SELECT student_id FROM studenti WHERE ime_prezime=?""", (ime_prezime, ))
        row = self.cur.fetchone()
        if row:
            return row[0]

     def dodaj_student(self, ime_prezime):
        self.cur.execute("""INSERT INTO studenti (ime_prezime) VALUES (?)""",(ime_prezime, ))
        self.conn.commit()
        return self.cur.lastrowid

     def promijeni_student(self, staro_ime, novo_ime):
        if(self.vrati_student_id(staro_ime)):
            self.cur.execute("""UPDATE studenti SET ime_prezime=? WHERE ime_prezime=?""",
                              (novo_ime, staro_ime))
            self.conn.commit()
        else:
            return None

     def izbrisi_student(self, ime_prezime):
        self.cur.execute("DELETE FROM studenti WHERE ime_prezime = ?", (ime_prezime, ))
        self.conn.commit()

     def ispitaj(self,student,kolegij,ocjena=None):
        if(ocjena==None):
            self.cur.execute("DELETE FROM ispiti WHERE student_id = ? AND kolegij_id=?",
                               (self.vrati_student_id(student),self.vrati_kolegij_id(kolegij) ))
            self.conn.commit()
        elif(ocjena):
               self.cur.execute("INSERT INTO ispiti (student_id, kolegij_id, ocjena) VALUES (?, ?,?)",
                               (self.vrati_student_id(student),self.vrati_kolegij_id(kolegij),ocjena))
               self.conn.commit()


     def svi_ispiti(self):
        self.cur.execute("""SELECT studenti.ime_prezime, kolegiji.naziv, ocjena FROM ispiti
                            JOIN studenti ON studenti.student_id=ispiti.student_id
                            JOIN kolegiji ON kolegiji.kolegij_id=ispiti.kolegij_id""")
        return self.cur.fetchone()

("*** TEST datoteka ***")
isp = Ispiti()
isp.dodaj("Ante Antic", "Linearna algebra", 5)
isp.dodaj("Ante Antic", "Programiranje 1", 4)
isp.dodaj("Marija Marijic", "Linearna algebra", 4)
isp.dodaj("Marija Marijic", "Matematicka analiza", 5)
#isp.spremi_datoteka("ispiti.txt")
print(open("ispiti.txt").read())
isp = Ispiti.ucitaj_datoteka("ispiti.txt")
print(isp)

print("*** TEST json ***")
isp = Ispiti()
isp.dodaj("Ante Antic", "Linearna algebra", 5)
isp.dodaj("Ante Antic", "Programiranje 1", 4)
isp.dodaj("Marija Marijic", "Linearna algebra", 4)
isp.dodaj("Marija Marijic", "Matematicka analiza", 5)
isp.spremi_json("ispiti.json")
print(open("ispiti.json").read())
isp = Ispiti.ucitaj_json("ispiti.json")
print(isp)

print('*** TEST SQLite studenti ***')
db = IspitiDB("ispiti.sqlite")
print(db.cur.execute("SELECT * FROM studenti").fetchall())
db.dodaj_student("Ante Antić")
db.dodaj_student("Ana Anić")
db.dodaj_student("Pero Perić")
print(db.cur.execute("SELECT * FROM studenti").fetchall())
print(db.vrati_student_id("Pero Perić"))
print(db.vrati_student_id("Marija Marijić"))
db.izbrisi_student("Pero Perić")
db.promijeni_student("Ana Anić", "Marija Marijić")
print(db.cur.execute("SELECT * FROM studenti").fetchall())

print('*** TEST SQLite ispiti ***')
db = IspitiDB("ispiti.sqlite")
db.dodaj_student("Ante Antić")
db.dodaj_student("Marija Marijić")
db.dodaj_kolegij("Linearna algebra")
db.ispitaj("Ante Antić", "Linearna algebra", 5)
print(db.svi_ispiti())
db.ispitaj("Ante Antić", "Linearna algebra", 4)
print(db.svi_ispiti())
db.ispitaj("Ante Antić", "Linearna algebra")
print(db.svi_ispiti())
db.ispitaj("Ante Antić", "Linearna algebra", 5)
db.ispitaj("Marija Marijić", "Programiranje 1", 5)
db.ispitaj("Marija Marijić", "Matematička analiza", 4)
print(db.svi_ispiti())