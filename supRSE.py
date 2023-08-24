"""
La RDD Pégase permet, via un mécanisme d'injection, de charger un fichier CSV directement dans une nomenclature du référentiel.
Mais il n'existe pas de commande pour remettre à zéro cette nomenclature et en refaire une nouvelle injection.
Il faut dans ce cas développer un logiciel pour supprimer les occurrences de cette nomenclature.
C'est ce que permet ce script Python pour :
    - se connecter
    - lister les régimes spéciaux d'étude (on prend ici les RSE comme exemple de nomenclature générique)
    - les supprimer tous pour préparer une nouvelle injection RDD
Laurent Abraham - 2023
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
else:
    raise Exception(response.status_code)

#
# Récupération de données
#

# Récupération de la nomenclature RegimeSpecialEtudes

URL = 'https://ref.'+instance+'.pc-scol.fr/api/v1/ref/nomenclatures/RegimeSpecialEtudes'
headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer ' + jeton
}
response = requests.get(URL, headers=headers)
if response.status_code != 200:
    raise Exception(response.status_code)
donnees = response.json()
print(f"{len(donnees)} occurrences dans la liste response")
for i in range(len(donnees)):
    print(f"{donnees[i]['code']} : {donnees[i]['libelleAffichage']}")

#
# Suppression de données
#

# Boucler sur les occurrences à supprimer
for i in range(len(donnees)):

    print(i)
    # Récupérer les informations de la nomenclature à supprimer
    d = dict(donnees[i])
    print(f"\n{d['code']} = {d['libelleAffichage']}\n")

    URL = 'https://ref.'+instance+'.pc-scol.fr/api/v1/ref/nomenclatures/RegimeSpecialEtudes/code/'+d['code']+'/dateDebutValidite/'+d['dateDebutValidite']+'/structure/ETAB00'
    #print(URL)
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer ' + jeton,
        'content-type': 'application/json'
    }
     response = requests.delete(URL, headers=headers)
    if response.status_code == 204:
        print("Response status code = ", response.status_code)
    else:
        raise Exception(response.status_code)

