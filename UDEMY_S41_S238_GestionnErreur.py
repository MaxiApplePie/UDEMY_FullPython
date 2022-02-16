a = 10
b = 1

try:
    r = (a / b)
except ZeroDivisionError:
    print('Division par zero')
except TypeError:
    print('Erreur de type')
except NameError:
    print('Probleme de variable')
else:
    print(r)