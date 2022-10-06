'''
Entre 0 y 1 años es junior
Entre 1 y 3 años es semi senior
Entre 3 y 5 años es senior
'''
anios=int(input("Cuántos años de experiencia tienes: "))
if 0 <= anios<1:
    print("Cadidato para ser junior")
elif 1 <= anios<3:
    print("Cadidato para ser semi senior")
elif 3 <= anios<5:
    print("Cadidato para ser senior")