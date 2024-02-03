import os

nomUtilisateur = input("Bonjour très cher personne, comment vous appelez vous? > ")
os.system('cls' if os.name == 'nt' else 'clear')

print("Bienvenue,", nomUtilisateur)

prixHT = input("Entrez un prix HT > ")
prixHT = int(prixHT)
os.system('cls' if os.name == 'nt' else 'clear')

taxeVoulu = input("Entrez la taxe a calculer sur le prix > ")
taxeVoulu = int(taxeVoulu)
os.system('cls' if os.name == 'nt' else 'clear')

prixTTC = prixHT + (prixHT * taxeVoulu / 100)

print("Le prix TTC est de", prixTTC, "euros")
print("Merci d'avoir utilisé mon logiciel !")
