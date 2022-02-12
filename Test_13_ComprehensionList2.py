#1_ Nombres pairs
nombres = [21, 44, 85, 98, 66, 1, 7]
nombres_pairs = [x for x in nombres if x % 2 == 0]
print(nombres_pairs)

# 2_ Nombres positifs
nombres = range(-10, 10)
nombres_positifs = [x for x in nombres if x >= 0]
print(nombres_positifs)

# 3_ Nombres multipliés par 2
nombres = range(5)
nombres_doubles = [2 * x for x in nombres]
print(nombres_doubles)

# 4 _ Les opposés.
nombres = range(10)
nombres_inverses = [x if x % 2 == 0 else -x for x in nombres]
print(nombres_inverses)

# Exo 26
nombres = range(51)
nombres_pairs = [x for x in nombres if x % 2 == 0]
print 
