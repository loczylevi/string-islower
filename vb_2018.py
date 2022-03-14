"""varos;nev1;nev2;ferohely
Moszkva;Luzsnyiki Stadion;n.a.;78011"""

class Vb_2018:
  def __init__(self,sor):
    sor = sor.strip().split(";")
    self.varos = sor[0]
    self.nev = sor[1]
    self.alternativ_nev = sor[2]
    self.ferohely = int(sor[3])

with open("vb2018.txt","r",encoding="latin2") as f:
  fejlec = f.readline()
  lista = [Vb_2018(sor) for sor in f]

#3
print(f"3.feladat: Stadionok száma: {len(lista)}")

#4
helyek = [sor.ferohely for sor in lista]
kicsi = helyek[0]
varos = ""
stadion = ""
for sor in lista:
  if kicsi > sor.ferohely:
    kicsi = sor.ferohely
    varos = sor.varos
    stadion = sor.nev

print(f"""4.feladat: A legkevesebb férőhely:
       Város: {varos}
       Stadion: {stadion}
       Férőhely: {kicsi}""")

#5
ossz = sum(helyek)
atlag = ossz / len(lista)

print(f"5.feladat: Átlagos férőhelyszám: {atlag:.1f}")
alternativ = len([sor.alternativ_nev for sor in lista])
szamol_na = len([sor.alternativ_nev for sor in lista if sor.alternativ_nev == "n.a."])

print(f"6.feladat: Két néven is ismert stadionok száma: {alternativ-szamol_na}")

#7
while True:
  bekeres = input("7.feladat: Kérek egy város nevet!\t")
  if bekeres.islower():
    bekeres = bekeres.capitalize()
  if bekeres.isupper():
    bekeres = bekeres.lower()
    bekeres = bekeres.capitalize()
  elif bekeres.isalpha():
    bekeres = bekeres.lower()
    bekeres = bekeres.capitalize()
  elif bekeres.isascii():
    bekeres = bekeres.lower()
    bekeres = bekeres.capitalize()
  if len(bekeres) >= 3:
    break

#8
kereso = [sor.varos for sor in lista if bekeres == sor.varos]

if len(kereso) > 0:
  print("8.feladat: A megadott város VB helyszín.")
else:
  print("8.feladat: A megadott város nem VB helyszín.")

#9
varosok = [sor.varos for sor in lista]
varos = varosok[0]
szamlalo = 1
for sor in lista:
  if varos != sor.varos:
    szamlalo = szamlalo + 1

print(f"9.feladat: {szamlalo} különböző városban voltak a mérkőzések")
