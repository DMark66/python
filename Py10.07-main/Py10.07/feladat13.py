print('Bankjegyautomata')

print('A legkisebb címlet 1000 Ft, a maximálisan felvehető összeg 300 000Ft ')

bekert_osszeg= int(input('Adja meg mekkora összeget kíván  felvenni! '))

print('A kiadott bankjegyek: ')


tizezred = (bekert_osszeg / 100) * 10000

print(f'{tizezred}')