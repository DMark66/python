tomeg = int(input('Adja meg a testsúlyát (kg): '))
magassag = float(input('Adja meg a magasságát (cm): ')) 

mag_hatvanya = magassag / 100

magassag = mag_hatvanya * mag_hatvanya

index_pont = tomeg / magassag
tti:float() = testtomeg / magassag ** 2


print('testsúlyosztályod: ')

if index_pont <= 16:
    print(f'{index_pont} nagyon sovány vagy!')

elif 16 < index_pont < 16.99:
    print(f'{index_pont} mérsékelt sovány vagy!')

elif 17 < index_pont < 18.49:
    print(f'{index_pont} Enyhe sovány vagy, többet eszel és meg vagy')

elif 18.5 < index_pont < 24.99:
    print(f'{index_pont} Egézséges vagy') 

elif 25 < index_pont < 29.99:
    print(f'{index_pont} Tulsúly bátyja kell egy étrend')

elif 30 < index_pont < 34.99:
    print(f'{index_pont} I.fokú elhízás, Ez nem jóúúú')

elif 35 < index_pont < 39.99:
    print(f'{index_pont} II.fokú elhízás íjj ez se jóúú')

elif 40 < index_pont:
    print(f'{index_pont} III.fokú elhízás')

  
print(' 1 adag túrós tonhalpástétom 15 dkg paradicsom és/vagy kígyóuborka, zöldpaprika, retek 1 bögre gyümölcstea édesítővel vagy üresen')


