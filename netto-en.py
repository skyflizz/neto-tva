#coding:utf-8

import os

nomUtilisateur = input("Hello dear person, what is your nickname? > ")
os.system('cls' if os.name == 'nt' else 'clear')

print("Welcome,", nomUtilisateur)

prixHT = input("Enter a price excluding VAT > ")
prixHT = int(prixHT)
os.system('cls' if os.name == 'nt' else 'clear')

taxeVoulu = input("Enter on 100 the tax added wanted > ")
taxeVoulu = int(taxeVoulu)
os.system('cls' if os.name == 'nt' else 'clear')

prixTTC = prixHT + (prixHT * taxeVoulu / 100)

print("The price includes VAT is", prixTTC, "Euros")
print("Thank you for using my software!")
