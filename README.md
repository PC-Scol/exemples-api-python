# exemples-api-python
Exemples de programmes Python pour interagir avec Pégase en utilisant ses API

Prérequis : disposer d'un environnement Python 3 (https://www.python.org/downloads/) et ajouter si nécessaire les modules requests et json

Module Pégase REF / API REF v1 - Référentiel :
- Le programme posEEEAccpays2.py permet de positionner la case à cocher Témoin UE EEE Accords sans passer manuellement par l'IHM Pégase pour chaque pays souhaité.
  - Utilisation des API :
    - GET ​/nomenclatures​/{codeNomenclature} Liste des nomenclatures
    - PUT ​/nomenclatures​/{codeNomenclature}​/code​/{code}​/dateDebutValidite​/{dateDebutValidite}​/structure​/{codeStructure} Modifier une nomenclature
  - Renseigner les variables password et instance dans le source pour adapter le programme Python à son instance Pégase
  - Adapter la liste de libellés courts dans le source Python à ses propres attentes (in [ "FRANCE", "ALLEMAGNE", "AUTRICHE", "BELGIQUE", ...])
- Le programme lstpays.py donne un exemple de programme permettant de lister une nomenclature à toutes fins utiles (ici Pays et nationalités).
  - Utilisation des API :
    - GET ​/nomenclatures​/{codeNomenclature} Liste des nomenclatures
  - Renseigner les variables password et instance dans le source pour adapter le programme Python à son instance Pégase
  - Adapter le print à ses besoins (format lecture ou CSV), choix des champs à lister (code, libelleCourt, libelleLong, etc., à trouver dans swagger)
  - C'est une sortie écran : pour créer un fichier, lancer par exemple python3 lstpays.py > lstpays.csv
- Le programme dumpdiplsise.py permet d'extraire au format CSV les codes diplômes SISE livrés avec Pégase (l'IHM ne permet pas de les parcourir facilement).
  - Utilisation des API :
    - GET ​/nomenclatures​/{codeNomenclature} Liste des nomenclatures
  - Renseigner les variables password et instance dans le source pour adapter le programme Python à son instance Pégase
