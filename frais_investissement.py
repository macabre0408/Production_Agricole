from math import ceil

def CalculerNombreSacs(quantiteSac:float, poidsSac:int=25)->int:
    return ceil(quantiteSac/poidsSac)


Taux_mortalite = {"Poulet chair":0.05, "Dindon":0.08, "Poule pondeuse":0.01}

def NbreVollaileApresTM(quantite_achete)->dict:
    qteApresTm={"Poulet chair":0, "Dindon":0, "Poule pondeuse":0}
    for key in quantite_achete.keys():
        qteApresTm[key]= round(quantite_achete[key]*(1-Taux_mortalite[key]))
    print(qteApresTm)
    return qteApresTm

def CoutAchat(quantite_achete):
    '''Calcul du cout total d'achat des volailles '''
    
    #prix des volailles: 
    prix_volaille = (2.25, 4.75, 15)
    prix_achat=0

    i=0 #index
    for k in quantite_achete.keys():
        prix_achat+=quantite_achete[k]*prix_volaille[i]
        i+=1
    return prix_achat

def CoutNourriture(qteApresTm)->float:
    
    '''Calcul du cout total de nourriture des volailles'''
    
    '''
    puisque les poules ont été acheté à 19 semaines et ne sont renouvellés qu'après une période de deux ans. Nous pouvons donc déterminer la quantité de nourriture qu'elles consommeront en 1 année entière si on suppose qu'elle consomme 6kg pour 4 semaines
    '''
    consommationAnnuellePoulePondeuse =52*6/4

    #nbre de sac poule pondeuse
    nbreSacPoulePondeuse = CalculerNombreSacs(qteApresTm['Poule pondeuse']*consommationAnnuellePoulePondeuse)

    #cout de la nourriture
    coutNourriturePoulePondeuse=21
    #prix de la nourriture des poules pondeuses:
    prixNourriturePoulePondeuse =  coutNourriturePoulePondeuse*nbreSacPoulePondeuse



    #Les données sur les poulets de chair :
    consommationPouletChair = (2, 4, 4)
    coutNourriturePouletChair =(20, 21, 21)
    abattagePouletChair =(1/3, 1/2, 0)
    pouletChair=qteApresTm["Poulet chair"]

    qtePouletChair=0
    nbreSacPouletChair=0
    prixNourriturePouletChair = 0
    for i in range(3):
        qtePouletChair=pouletChair*consommationPouletChair[i] #qte total consommé par période 
        nbreSacPouletChair=CalculerNombreSacs(qtePouletChair)
        prixNourriturePouletChair+=nbreSacPouletChair*coutNourriturePouletChair[i]#prix de la nourriture
        pouletChair = pouletChair-round(pouletChair*abattagePouletChair[i])#nombre de poulet après abattage


    

    #Les données sur les dindons :

    #équivalent de la consommation pour une période de 5 semaine (14 a 19):
    consommationAnnuelleDindon= 5*11/4
    consommationDindon = (3, 5, 5, 11, consommationAnnuelleDindon)
    coutNourritureDindon=(22,23,23,23,23)

    qteDindon=0
    nbreSacDindon=0
    prixNourritureDindon=0

    for i in range(5):
        qteDindon=qteApresTm['Dindon']*consommationDindon[i]
        nbreSacDindon=CalculerNombreSacs(qteDindon)
        prixNourritureDindon+=nbreSacDindon*coutNourritureDindon[i]
    
    return prixNourriturePoulePondeuse+ prixNourriturePouletChair +prixNourritureDindon

def CalculerCoutRip(qteApresTm)->float:   
    '''Calcul du cout total de la ripaille des volailles'''
    sacParSemaine = (1, 1, 1/3)
    prixSacRip = 9
    dureeElevage=(10, 19, 52)
    nombreVolailles=tuple(qteApresTm.values())
    espaceVie = (1.25, 3, 1)
    abattagePouletChair =(1/3, 1/2, 0)
    nbreSacTotal=0
    
    periodeElevagePouletChair =(4, 4, 2)
    
    nbreSacPouletChair=0
    
    
    for i in range(3):
        #Nbre de sac de rip pour les poulets de chair
        nbrePouletChair=nombreVolailles[0] #représente le nombre actuelle de poulets de chair
        
        nbreSacPouletChair+=nbrePouletChair*espaceVie[0]*sacParSemaine[0]*periodeElevagePouletChair[i]
        
        nbrePouletChair=nbrePouletChair-round(nbrePouletChair*abattagePouletChair[i]) #le reste des poulets de chair après abattage
        
    #rip pour les autres volailles
    for i in range(1,3):
        nbreSacTotal+=nombreVolailles[i]*espaceVie[i]*sacParSemaine[i]*dureeElevage[i]    #nombre de sac pour toute la durée de l'élevage
        
    return ceil(nbreSacTotal+nbreSacPouletChair)*prixSacRip  #Coût total de la rip

