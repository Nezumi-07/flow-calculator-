# flow-calculator-

# Calculateur de débit de perfusion (v0)

Petit programme en console, écrit pour m'entraîner en Python et pour vérifier mes calculs de dose pendant mes révisions d'IFSI.

!!! **Outil d'entraînement uniquement : à ne pas utiliser pour de vrais soins.** !!! 
Il ne dispense pas d'une vérification humaine et ne détecte ni interactions médicamenteuses ni erreurs de prescription.

## Ce que fait la v0
- Calcule le volume à prélever pour chaque médicament (dose × volume de l'ampoule ÷ quantité).
- Calcule le débit d'une perfusion en gouttes/min (gouttes/mL × volume total ÷ durée en minutes).

## Lancer le programme
Python 3 requis, aucune bibliothèque à installer

## Exemple
500 mg prescrits, ampoule de 1 000 mg pour 10 mL, poche de 250 mL, 20 gouttes/mL, durée 0,5 h
→ 5 mL à prélever, débit de 170 gouttes/min.

## Hypothèses
- Doses en mg, volumes en mL.
- Volume total = volume de la poche + volume du médicament ajouté.

## Limites connues (v0)
- Aucune vérification des saisies : le programme plante sur du texte, un 0, ou une virgule dans la durée.
- Le menu demande une saisie exacte.
- Seule la perfusion est disponible (SAP, PSE et transfusion à venir).

## Prochaines versions
Vérification des saisies, convertisseur d'unités, SAP et PSE, tests.
