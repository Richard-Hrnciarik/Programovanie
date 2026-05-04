subor = open('dopravny_prieskum.txt', 'r')

cestujuci = 0
velkost = 'kratka'
automaty = []
na_znamenie = []
for riadok in subor:
    riadok = riadok.strip()
    bodkociarka1 = riadok.find(';')
    bodkociarka2 = riadok.rfind(';')
    nastupili = riadok[:bodkociarka1]
    if int(nastupili) >= 10:
        automaty.append(riadok[bodkociarka2 + 1:])
    vystupili = riadok[bodkociarka1 + 1:bodkociarka2]
    if (int(nastupili) < 3 or int(vystupili) < 3) and ((int(vystupili) + int(nastupili)) < 6):
        na_znamenie.append(riadok[bodkociarka2 + 1:])
    cestujuci = cestujuci + int(nastupili) - int(vystupili)
    print(riadok[bodkociarka2 + 1:] + ' - pocet cestujucich: ' + str(cestujuci) + ' odporucana velkost elektricky: ' + velkost)
    if cestujuci < 20:
        velkost = 'kratka'
    elif cestujuci < 75:
        velkost = 'stredna'
    else:
        velkost = 'dlha'

print('Zastavky, kde je vhodne osadit automat:')
for riadok2 in automaty:
    print(riadok2)

print('Zastavky len na znamenie')
for riadok3 in na_znamenie:
    print(riadok3)

subor.close()
#Ak treba obmedzit aj celkovo v podmienke treba zmenit celkovo > 6 na > 3
