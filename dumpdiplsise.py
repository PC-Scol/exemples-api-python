"""
Les codes diplôme SISE sont intégrés nativement à Pégase. Leur grand nombre rend la consultation
en ligne difficile (limitation du nombre d'occurrences affichées).
Ce script Python permet de :
    - se connecter
    - lire les diplômes SISE dans Pégase
    - vider les diplômes SISE dans un fichier CSV
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

# Récupération de la nomenclature Diplômes SISE

URL = 'https://ref.'+instance+'.pc-scol.fr/api/v1/ref/nomenclatures/DiplomeSise'
headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer ' + jeton
}
response = requests.get(URL, headers=headers)
if response.status_code != 200:
    raise Exception(response.status_code)
donnees = response.json()
# Ecrire les données Diplômes SISE dans un fichier
with open("diplsise.csv","w", encoding='utf-8') as fdiplsise:
#    fdiplsise.write(json.dumps(donnees))
    # Ecrire la ligne d'en-têtes
    if len(donnees) > 0:
        # Convertir le JSON en dictionnaire pour bénéficier de la lecture des clés
        d0 = dict(donnees[0])
        fdiplsise.write(';'.join(d0.keys())+'\n')
    # Ecrire les lignes de valeurs
    for i in range(len(donnees)):
        # Convertir le JSON en dictionnaire pour bénéficier de la lecture des valeurs
        d = dict(donnees[i])
        # Convertir en liste pour parcourir les valeurs et convertir les int en str
        # pour permettre l'utilisation de la fonction join()
        l = list(d.values())
        for j in range(len(l)):
            l[j] = str(l[j])
        fdiplsise.write(';'.join(l)+'\n')
