import os


def main():
    print("*****************CALCULATEUR DE MOYENNE*****************")

    message = "Veuillez saisir 'Add' pour ajouter à la liste ou appuyer sur 'Calcul' pour calculer la moyenne :"
    listNum = []

    while True:
        query = input(message)

        if query == "Add" or query == "add" or query == "A" or query == "A":
            number = int(input("Veuillez entrer un chiffre/nombre :"))
            listNum.append(number)

            print(listNum)
        elif query == "Calcul" or query == "calcul" or "C" or query == "C":
            if not listNum:
                print("La liste ne peut pas être vide !")
                break

            listNumCount = len(listNum)

            print("Liste de chiffre/nombre :", listNum)
            print("Votre nombre total d'éléments dans la liste : ", listNumCount)
            print("Votre moyenne est de " + str(sum(listNum) / listNumCount) + "/20")
            break
        else:
            print(message)

    print("********************************************************")
    os.system("pause")


if __name__ == '__main__':
    main()
