from tinydb import TinyDB
db = TinyDB('user.json')

db.insert({'first_name':'Otabek','last_name':'Abdurasulov','job':'Student'})
db.insert({'first_name':'Sardor','last_name':'Muminjonov','job':'Student'})