print('Utazási költségtérités')

megtettut= float(input('Add meg a megtett utat km-ben! '))
autofogyaszt= float(input('Add meg az autó fogyasztását 100 km-re literben! '))
uzemanyagar= float(input('Add me az üzemanyagárat ft-ban! '))

uzemanyagkoltseg = (megtettut * autofogyaszt * uzemanyagar) / 100

if megtettut > uzemanyagkoltseg:
    print(f'{uzemanyagkoltseg} + {megtettut * 25}')
else:
    print(f'Költségtérités: {uzemanyagkoltseg} Ft.')
