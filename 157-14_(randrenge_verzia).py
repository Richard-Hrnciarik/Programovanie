from random import *
cislo = input('Zadaj číslo, ktoré si myslíš a ja ho uhádnem. ')
dolna_hranica = input('Zadaj dolnú hranicu: ')
horna_hranica = input('Zadaj hornu hranicu: ')

vysledok = 0
pocet_pokusov = 0
while vysledok != int(cislo):
    vysledok = randrange(int(dolna_hranica), int(horna_hranica))
    if vysledok == int(cislo):
        pocet_pokusov += 1
        print('Tvoje cislo je: ' + str(vysledok) + ' uhadol som ho na pokus ' + str(pocet_pokusov))
    else:
        pocet_pokusov += 1
    