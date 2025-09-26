cislo = input('Zadaj číslo, ktoré si myslíš a ja ho uhádnem. ')
dolna_hranica = input('Zadaj dolnú hranicu: ')
horna_hranica = input('Zadaj hornu hranicu: ')

pocet_pokusov = 0
for i in range(int(dolna_hranica), int(horna_hranica)):
    if i == int(cislo):
        pocet_pokusov += 1
        print('Tvoje cislo je: ' + str(i) + ' uhadol som ho na pokus ' + str(pocet_pokusov))
    else:
        pocet_pokusov += 1
        #print(pocet_pokusov)