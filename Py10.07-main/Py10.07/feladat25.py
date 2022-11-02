szam1 = int(input('Az első szám: '))
szam2 = int(input('A második szám: '))
muv_jel = input("Adja meg a műveleti jelet ezek közül +,-,*,/: ")


if muv_jel == '+':
    eredmény = szam1 + szam2
elif muv_jel == '-':
    eredmény = szam1 - szam2
elif muv_jel == '*':
    eredmény = szam1 * szam2
elif muv_jel == '/':
    eredmény = szam1 / szam2
else:
    print("Hibás adatok")

print(szam1, muv_jel , szam2, "=", eredmény)
