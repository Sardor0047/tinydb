from tinydb import TinyDB
import requests
db = TinyDB('user.json')

db_random =TinyDB('random_user.json')


url = "https://randommer.io/api/Name?nameType=firstname&quantity=5"

headers = {
    "X-Api-Key": 'b9684522e39c47ab9cd0a655122028a5' 
}
response = requests.get(url,headers=headers)
r = response.json()
for user in r:
    db_random.insert({'name':f"{user}"})
