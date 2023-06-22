"""
Pégase ne comprend pas (encore) de fonctionnalités d'export des données contenues dans les tableaux de l'IHM.
Il est possible d'effectuer un export des données au format JSON à partir des plates-formes swagger, puis de
transformer ce fichier JSON en format CSV.
Mais pour extraire directement une partie des colonnes sans passer par cette étape JSON, un programme Python
peut lire les données via la API Pégase et en sortir tout ou partie à l'écran.
L'exemple ci-dessous est basé sur la nomenclature "Pays et nationalités" qui contient la liste de tous les pays.

Script Python pour :
    - se connecter
    - récupérer le jeu de données (en JSON) : les Pays et nationalités
    - lister les Pays et nationalités
Laurent Abraham - 2023 - Université de Rennes
"""
import requests
import json

#
# Partie variable selon les environnements Pégase
#
# 1. Renseigner les passwords avec les informations prises dans le coffre de l'établissement fourni par PC-Scol
# 2. Remplacer <inst-etab> avec le nom de l'instance tel qu'il apparaît dans les URL Pégase age....
"""
# Environnement test
username = 'svc-api'
password = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
instance = 'test-<inst-etab>'
# Environnement pilote
username = 'svc-api'
password = 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY'
instance = 'pilote-<inst-etab>'
"""
# Environnement bac à sable
username = 'svc-api'
password = 'ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ'
instance = 'bas-<inst-etab>'

#
# Connexion à Pégase
#

URL = 'https://authn-app.'+instance+'.pc-scol.fr/cas/v1/tickets'
response = requests.post(
    URL,
    headers={'content-type': 'application/x-www-form-urlencoded'},
    data={'username': username, 'password': password, 'token': 'true'}
)
if response.status_code == 201:
    jeton = response.text
#    print('Token = ' + response.text)
else:
    raise Exception(response.status_code)

#
# Récupération de données
#

# Récupération de la nomenclature Pays et nationalités

URL = 'https://ref.'+instance+'.pc-scol.fr/api/v1/ref/nomenclatures/PaysNationalite'
headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer ' + jeton
}
response = requests.get(URL, headers=headers)
if response.status_code != 200:
    raise Exception(response.status_code)
donnees = response.json()

# Boucler sur les données pour les afficher à l'écran (ici, seulement le code, le libellé d'affichage, le continent et la nationalité)

for i in range(len(donnees)):
    # Sortie pour lecture
    print(f"Pays {donnees[i]['code']} : {donnees[i]['libelleAffichage']}, continent {donnees[i]['continent']} (nationalité {donnees[i]['libelleNationalite']})")
    # Sortie au format CSV
    #print(f"{donnees[i]['code']};{donnees[i]['libelleAffichage']};{donnees[i]['continent']};{donnees[i]['libelleNationalite']}")

