# Практическая работа "Индекс массы тела"

print('Tere! Olen sinu uus sõber - Python!')
nimi = input('Mis Sinu nimi on?: ')
indeks = None
print('Oi kui ilus nimi!')
try:
    vastu = int(input(f'{nimi}! Kas leian Sinu keha indeksi? Palun vasta 0=ei või 1=jah: '))
    if vastu ==0:
        print(f'Kahju! See on väga kasulik info!')
    elif vastu != 1:
        print('See ei ole õige vasta')
        SystemExit
    else:
        pikkus = int(input('Sissestage oma pikkus: '))
        mass = float(input('Sissestage oma mass: '))
    if vastu == 1:
        indeks = mass/(0.01*pikkus)**2
        if indeks < 16:
            print(f'{nimi}! Sinu keha indeks on: {round(indeks, 1)}. Tervisele ohtlik alakaal.')
        elif indeks == 16 or indeks < 19:
            print(f'{nimi}! Sinu keha indeks on: {round(indeks, 1)}. Alakaal.')
        elif indeks == 19 or indeks < 25:
            print(f'{nimi}! Sinu keha indeks on: {round(indeks, 1)}. Normaalkaal.')
        elif indeks == 25 or indeks < 30:
            print(f'{nimi}! Sinu keha indeks on: {round(indeks, 1)}. Ülekaal.')
        elif indeks == 30 or indeks < 35:
            print(f'{nimi}! Sinu keha indeks on: {round(indeks, 1)}. Rasvumine.')
        elif indeks == 35 or indeks < 40:
            print(f'{nimi}! Sinu keha indeks on: {round(indeks, 1)}. Tugev rasvumine.')
        elif indeks == 40 or indeks > 40:
            print(f'{nimi}! Sinu keha indeks on: {round(indeks, 1)}. TTervisele ohtlik rasvumine.')
    print(f'\nKohtumiseni, {nimi}! Igavesti Sinu, Python!')
except:
    ValueError
    print(f'See ei ole õige vasta\n\nKohtumiseni, {nimi}! Igavesti Sinu, Python!')