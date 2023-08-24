"""
Script Python pour :
    - se connecter
    - lister les régimes spéciaux d'étude
    - les supprimer pour préparer une nouvelle injection RDD
Laurent Abraham - 2023
"""
import requests
import json

#
# Partie variable selon les environnements Pégase
#
"""
# Environnement bac à sable
username = 'svc-api'
password = 'YZIgVeyDXmDAofeaTrYRAmzlzAAbalRlvMMUsIPD'
instance = 'bas-univ-rennes1'
# Environnement test
username = 'svc-api'
password = 'osOxvjOtJCFlXEiSqCCEuSzMwflahnLOwxXYRDrq'
instance = 'test-univ-rennes1'
# Environnement RDD
username = 'svc-api'
password = 'BaRRbgCWptvxHTHVKSIuORatAAmjGIwOWJIoUguI'
instance = 'rdd-univ-rennes1'
# Environnement pilote
username = 'svc-api'
password = 'diXdxgGGEKprKPEtfgIaolCOmPRFgXawpjhmRGTn'
instance = 'pilote-univ-rennes1'
"""
# Environnement RDD
username = 'svc-api'
password = 'BaRRbgCWptvxHTHVKSIuORatAAmjGIwOWJIoUguI'
instance = 'rdd-univ-rennes1'

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

# Récupération de la nomenclature RegimeSpecialEtudes

URL = 'https://ref.'+instance+'.pc-scol.fr/api/v1/ref/nomenclatures/RegimeSpecialEtudes'
headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer ' + jeton
}
response = requests.get(URL, headers=headers)
if response.status_code == 200:
    print("Response status code = ", response.status_code)
#    print(response.json())
else:
    raise Exception(response.status_code)
donnees = response.json()
print(f"{len(donnees)} occurrences dans la liste response")
#print(type(donnees)) : donnees est de type list
"""
for i in range(len(donnees)):
    print(f"{donnees[i]['code']} : {donnees[i]['libelleAffichage']}")
"""
#
# Modification de données
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

