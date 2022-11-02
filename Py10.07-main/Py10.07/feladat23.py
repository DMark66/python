pontszam = int(input('Adja meg az elért pontszámot: '))

if pontszam < 42:
    print('elégtelen')
elif pontszam < 57:
    print('elégséges')
elif pontszam < 72:
    print('közepes')
elif pontszam < 87:
    print('jó')
else:
    print('jeles')

