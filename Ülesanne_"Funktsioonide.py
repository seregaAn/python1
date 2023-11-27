# Ülesanne "Funktsioonide print(),input(), float(), int() kasutamine"

# 1
from statistics import mean
import math
print("Tere, maailm!")
nimi = input("Mis sinu nimi on?: ")
print("Tere, maailm! Tervitan sind " + nimi)
vanus = input("Sinu vanus on? ")
print("Tere, maailm! Tervitan sind " + nimi +
      ". Sa oled " + vanus + " aastat vana.")

# 2
vanus_1 = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis = True

print(type(vanus_1))
print(type(eesnimi))
print(type(pikkus))
print(type(kas_käib_koolis))

# 3
kommid = 40
minus_kommid = int(input("Laual on 40 kommid. Mitu kommi sina võtta tahad?: "))
jääk = kommid - minus_kommid
print("Nüüd laual on " + str(jääk) + " kommid")

# 4
Ümbermõõt = float(input("Mis on ümbermõõt \"sm\"?; "))
läbimõõt = Ümbermõõt / (math.pi)
print("Puu läbimõõt on " + str(läbimõõt) + "sm")

# 5
a = float(input('Mis on krundi esimese külje pikkus \"m\"?: '))
b = float(input('Mis on krundi teinee külje pikkus \"m\"?: '))
c = (math.hypot(a, b))
print("Ristkülikukujulise maatüki diagonaal on " + str(math.trunc(c)) + " m")

# 6
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus / aeg
print("Sinu kiirus oli " + str(kiirus) + " km/h")

# 7

a = float(input("Esimene  arv: "))
b = float(input("Teine  arv: "))
c = float(input("Kolmas  arv: "))
d = float(input("Neljas  arv: "))
e = float(input("Viies  arv: "))
print("Aritmeetiline keskmine " + str(mean([a, b, c, d, e])))

# 8
print('  @..@\n (----)\n (\\__/) \n^^ "" ^^ ')

# b variant;)
print('''           @..@
          (----)
          (\\__/) 
         ^^ "" ^^ ''')

# 9
kolmnurga_külg_1 = 10
kolmnurga_külg_2 = 25
kolmnurga_külg_3 = 45
print(kolmnurga_külg_1+kolmnurga_külg_2+kolmnurga_külg_3)

# 10
kogu_makse = 12.9
tipp = 0.1


def sum_nums(a, b, c):
    sum = ((a+a*b)/c)
    return sum


first_sum = sum_nums(kogu_makse, tipp, 2)
print('Kõik peavad maksma ' + str(round(first_sum, 2)) + '€')
