    #l'objectif de ce code est d'avoir un calculateur de débit de perfusion.

from fractions import Fraction
                            
def calcul_volume_a_prelever():
    volume_medicament = 0
    nombre_medicament = int(input("Combien de médicaments sont utilisés?  : "))
    for i in range (nombre_medicament):
        nom_medicament = input("Nom du médicament prescrit : ")
        print ("* Rappel : 1g=1000mg")
        dose_prescrite = float(input ("Dose prescrite (en mg) :  ") )
        print ("Merci d'indiquer les informations concernant le dosage de l'ampoule / du flacon / du produit reconstitué")
        print ("* Rappel : pour les concentrations en pourcent, x% donne x g pour 100ml.")
        quantite_medicament = float(input("Combien de mg? : "))
        volume_ampoule = float(input ("Pour combien de mL? : "))
        volume_a_prelever = dose_prescrite*volume_ampoule/quantite_medicament
        volume_medicament = volume_medicament + volume_a_prelever
        print (f"Vous devez prélever {volume_a_prelever} mL de /d' {nom_medicament}")
        print("— — — —")
    print(f"Volume total de médicament à prélever {volume_medicament} mL")
    print("— — — —")
    return volume_medicament

def perf():
    volume_medicament = calcul_volume_a_prelever()
    nom_solvant = input(" Quel solvant utilisez-vous? : ")
    print ("* Rappel : pour une solution aqueuse (NaCl, glucosé, Ringer-lactate...), on considère comme facteur 20 gouttes/mL ")
    nombre_goutte_par_millilitres = int(input("Combien de gouttes/mL ? : "))
    volume_solvant = float(input("Quel est le volume de votre poche? (en mL) : "))
    print ("* Rappel : 20 min = 1/3, 30 min = 0.5h, 45 min = 0,75h")
    duree_perf = float(Fraction(input("Durée de la perfusion (en h) : ")))
    volume_total = volume_solvant + volume_medicament
    debit_perf = nombre_goutte_par_millilitres * volume_total / (60*duree_perf)
    print("—")
    print (f"Le débit de votre perfusion est de : {debit_perf} gouttes/min")
    print("— — — —")
    return debit_perf
        
def choix_type_IV():
    type_IV= input("Quel type de préparation faites-vous? perfusion, seringue auto-pulsée (SAP), pousse seringue électrique (PSE)")
    if type_IV == "perfusion" or type_IV == "perf":
        perf()
    elif type_IV == "seringue auto-pulsee" or type_IV == "seringue autopulsée" or type_IV == "SAP" or type_IV == "sap" :
        print ("Indisponible pour le moment, programme en construction :) ")
        main()
    elif type_IV == "pousse seringue électrique " or type_IV == "pousse seringue electrique" or type_IV == "PSE" or type_IV == "pse" :
        print ("Indisponible pour le moment, programme en construction :) ")
        main()
    else: 
        print ("Je n'ai pas compris votre choix, veuillez réessayer.")
        choix_type_IV()
        
        
def main():
    print ("Ceci est un outil pour calculer un débit de perfusion, mais ne dispense pas d'une vérification humaine.")
    print(" Il ne vérifie pas les interactions médicamenteuses.")
    print("Merci de donner uniquement les informations demandées, uniquement en chiffres s'il s'agit d'une valeur numérique, et dans l'unité demandée")
    print("*Actuellement utilisable uniquement pour les perfusions")
    print("*À venir : Seringue auto-pulsée, PSE, transfusion...")
    choix_type_IV()        
        
main()           