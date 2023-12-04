import requests
response = requests.post(url='https://api.pokemonbattle.me:9104/pokemons', 
              json={
                   "name": "Grekh",
                   "photo": "https://dolnikov.ru/pokemons/albums/084.png",
},
                   headers={'Content-Type': 'application/json',  
                   'trainer_token': '5aa56b5ccb150cbdb436ead42916cd92'})
print(response)

response = requests.put(url='https://api.pokemonbattle.me:9104/trainers', 
              json={
                   "name": "Grekulya",
                   "city": "Aktobe"
},
                   headers={'Content-Type': 'application/json',  
                   'trainer_token': '5aa56b5ccb150cbdb436ead42916cd92'})
print(response)


response = requests.post(url='https://api.pokemonbattle.me:9104//trainers/add_pokeball', 
              json={"pokemon_id": "21161"             
},
                   headers={'Content-Type': 'application/json',  
                   'trainer_token': '5aa56b5ccb150cbdb436ead42916cd92'})
print(response)