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
 
