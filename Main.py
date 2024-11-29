#AGBLOYOE Oladé Jules Junior
#DARIUS Shaun

from frais_investissement import *


quantite_achete = {"Poulet chair":0, "Dindon":0, "Poule pondeuse":0}


print("Titre : Programme de gestion automatisé élevage volailles")
print("Entrée les quantités de volailles achetées")

for key in quantite_achete.keys():
    quantite_achete[key]=int(input(f"Veuillez entrer la quantité de {key} : "))

qte_volaille = NbreVollaileApresTM(quantite_achete)

for i in range(5,1,-1):
    print('*'*i)
print("\t1- Calcul des frais d'investissement initiales")
print("\t2- Calcul de la quantité d'oeufs produite")
print("\t3- Calcul du revenu")
print("\t4- La dernière journée d'élevage des volailles")

choix=int(input("Veuillez entrer votre choix: "))

if choix==1:
    print("Le coût d'achat des volailles revient à : ",CoutAchat(quantite_achete),"$")
    print(f"Le coût de la moulée des volailles s'élève à {CoutNourriture(qte_volaille)}$")
    print(f"Le coût de la ripaille des volailles s'élève à {CalculerCoutRip(qte_volaille)}$")
    print(f"Les frais total d'investissement s'élèvent donc à {CoutAchat(quantite_achete)+CoutNourriture(qte_volaille)+CalculerCoutRip(qte_volaille)}$")
elif choix ==2:
    print("####")
elif choix ==3:
    print("####")
elif choix ==4:
    print("####")