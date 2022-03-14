#�v;Elem;Vegyjel;Rendsz�m;Felfedez�

#1250;Arz�n;As;33;Albertus Magnus

#1-2

class Kemia:
  def __init__(self,sor):
    ev,elem,vegyjel,rendszam,felfedezo = sor.strip().split(";")
    self.ev = ev
    self.elem = elem
    self.vegyjel = vegyjel
    self.rendszam = int(rendszam)
    self.felfedezo = felfedezo

with open("felfedezesek.csv","r",encoding="latin2") as f:
  fejlec = f.readline()
  lista = [Kemia(sor) for sor in f]

#3
  
print(f"3.feladat: Elemek száma: {len(lista)}")

#4

okor = len([sor.ev for sor in lista if sor.ev == "Ókor"])

print(f"4.feladat: Felfedezések száma az ókorban: {okor}")

#5

while True:
  bekeres = input("5.feladat: Kérek egy vegyjelet: ")
  if bekeres.isupper():
    bekeres = bekeres.lower()
    bekeres = bekeres.capitalize()
  if len(bekeres) == 1 and bekeres.isalpha():
    bekeres = bekeres.capitalize()
    break
  elif len(bekeres) == 2 and bekeres.isalpha():
    bekeres = bekeres.capitalize()
    break

#6

kereso = [sor for sor in lista if sor.vegyjel == bekeres]

if len(kereso) > 0:
  elem = kereso[0]
  print(f"""6.feladat: Keresés
       Az elem vegyjele: {elem.vegyjel}
       Az elem neve: {elem.elem}
       Az elem rendszáma: {elem.rendszam}
       Felfedezés éve: {elem.ev}
       Felfedező: {elem.felfedezo}""")
else:
  print("""6.feladat: Keresés
       Nincs ilyen elem az adat forrásban!""")

print("7.feladat: passz")

statisztika = dict()
evek = [ int(sor.ev) for sor in  lista if sor.ev != 'Ókor']  
for ev in evek:
    statisztika[ev] = statisztika.get(ev, 0) + 1

print(        f'8. feladat: Statisztika')
res = [ print(f'        {ev} - {elemek_száma} db') for ev, elemek_száma in statisztika.items() if elemek_száma > 3]
