import math
Aoldal = int(input('Add meg az A oldal hosszát (cm) : '))
Boldal = int(input('Add meg a B oldal hosszát (cm) : '))

Coldal_negyzet = (Aoldal * Aoldal) + (Boldal * Boldal)

Coldal = math.sqrt(Coldal_negyzet)

print(f'A C oldal: {Coldal}')
