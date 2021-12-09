import csv


def fn_question(question):
    return input(question)


def fn_encode(marque, modele, couleur, cylindre, motorisation, annee_de_production):
    file_csv = "test.csv"
    header = ["marque", "modele", "couleur", "cylindre", "motorisation", "annee_de_production"]
    data = [marque, modele, couleur, cylindre, motorisation, annee_de_production]
    with open(file_csv, "w", encoding="utf-8", newline="") as fichier:
        writer = csv.writer(fichier)
        writer.writerow(header)
        writer.writerow(data)


def fn_est_ancetre(annee):
    if int(annee) >= 25:
        return True
    else:
        return False


marque = fn_question("quel est la marque ?")
modele = fn_question("quel est le modele ?")
couleur = fn_question("quel est la couleur")
cylindre = fn_question("quel est le cylindre")
motorisation = fn_question("quel est la motorisation")
annee_de_production = fn_question("quel est l'annee_de_production")

fn_encode(marque, modele, couleur, cylindre, motorisation, annee_de_production)

if fn_est_ancetre(annee_de_production):
    print(marque, modele, "est ancetre")
else:
    print(marque, modele, "est pas un ancetre")