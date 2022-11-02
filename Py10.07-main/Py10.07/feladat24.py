helyseg = input('Adjon a helységnevet: ')
lelekszam = int(input('Adja meg a helység lélekszámát: '))

if lelekszam <= 0:
    print('hibás adatbevitel')
elif lelekszam < 5000:
    print(f'{helyseg}, egy közszég, mert a lélekszáma {lelekszam}')
elif lelekszam >= 5000 and lelekszam < 20000:
    print(f'{helyseg}, ez egy kisváros, mert a lélekszáma {lelekszam}')
elif lelekszam >= 20000 and lelekszam < 100000:
    print(f'{helyseg} egy középváros, mert a lélekszáma {lelekszam}')
elif lelekszam >= 100000 and lelekszam < 1000000:
    print(f'{helyseg} egy nagyváros, mert a lélekszáma {lelekszam}')
elif lelekszam >= 1000000:
    print(f'{helyseg} egy metropolis, mert a lélekszáma {lelekszam}')
