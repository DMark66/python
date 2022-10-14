auto_fogyaszt = int(input('Adja meg az autó fogyasztását 100 Km-en (liter): '))

benzinar = int(input('add meg a benzin árát: '))

megut = int(input('Add meg a hátralévő út hosszát: '))

vegar = (auto_fogyaszt * benzinar) + (benzinar * megut)

print(f'Az útiköltséged: {vegar}')
