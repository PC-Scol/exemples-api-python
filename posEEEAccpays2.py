"""
Dans le référentiel Pégase, la nomenclature "Pays et nationalités" contient la liste de tous les pays.
Pour chaque pays, une case à cocher "Témoin UE EEE Accords" permet de savoir si le pays doit être pris
en compte ou non pour le calcul des droits différenciés.
Ce programme Python permet de cocher/décocher toutes les cases souhaitées sans passer manuellement sur chaque entrée.

Script Python pour :
    - se connecter
    - récupérer le jeu de données (en JSON) : les Pays et nationalités
    - modifier les données : (dé)cocher la case Témoin UE EEE Accords des pays
    - les récrire dans l'environnement Pégase après modification
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
print(f"{len(donnees)} occurrences (pays) dans la liste response")
#
# Modification de données
#

# Boucler sur les occurrences à modifier
for i in range(len(donnees)):

# Ne positionner le témoin UE EEE Accords à vrai que pour les pays souhaités
# Liste à éventuellement mettre à jour selon l'établissement
    temoinAccords = donnees[i]['libelleCourt'] in [ "FRANCE", "ALLEMAGNE", "AUTRICHE", "BELGIQUE", "BULGARIE", "CHYPRE", "CROATIE", "DANEMARK", "ESPAGNE", "ESTONIE", "FINLANDE", "GRECE", "HONGRIE", "IRLANDE", "ITALIE", "LETTONIE", "LITUANIE", "LUXEMBOURG", "MALTE", "PAYS-BAS", "POLOGNE", "PORTUGAL", "TCHEQUIE", "ROUMANIE", "SLOVAQUIE", "SLOVENIE", "SUEDE", "SUISSE", "ISLANDE", "NORVEGE", "LIECHTENST", "MONACO", "ANDORRE" ]

    # On inclut un pays dans les pays de la zone UE EEE Accords en cochant cette case
    d = dict(donnees[i])
    print(f"{d['code']} = {d['libelleAffichage']} : ", end="")
    print(f"Témoin UE EEE Accords = {d['temoinAccords']} --> ", end="")
    d['temoinAccords'] = temoinAccords
    print(f" {d['temoinAccords']}")

    URL = 'https://ref.'+instance+'.pc-scol.fr/api/v1/ref/nomenclatures/PaysNationalite/code/'+d['code']+'/dateDebutValidite/'+d['dateDebutValidite']+'/structure/ETAB00'
#    print(URL)
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer ' + jeton,
        'content-type': 'application/json'
    }
    # Ne pas oublier le json.dumps pour revenir à du texte
    response = requests.put(URL, headers=headers, data=json.dumps(d))
    if response.status_code != 200:
        raise Exception(response.status_code)

