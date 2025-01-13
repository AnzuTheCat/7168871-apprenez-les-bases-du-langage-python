# Ecrivez votre code ici !
nombre1 = input("Entrez le premier nombre: ")
nombre2 = input("Entrez le deuxième nombre: ")

if nombre1.isnumeric() and nombre2.isnumeric() == False:
    raise SystemExit("Vous devez entrer des nombres entiers.")
else:
    nombre1 = int(nombre1)
    nombre2 = int(nombre2)

operation = input("Entrez l'opération à effectuer (+, -, *, /): ")

if operation not in ["+", "-", "*", "/"]:
    raise SystemExit("L'opération doit être une addition (+), une soustraction (-), une multiplication (*) ou une division (/).")
else:
    if operation == "+":
        resultat = nombre1 + nombre2
    elif operation == "-":
        resultat = nombre1 - nombre2
    elif operation == "*":
        resultat = nombre1 * nombre2
    elif operation == "/":
        if nombre2 == 0:
            raise SystemExit("La division par zéro est impossible.")
        else:
            resultat = nombre1 / nombre2
print(f"Le résultat de l'opération {nombre1} {operation} {nombre2} est égal à {resultat}.")
