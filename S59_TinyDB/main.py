from tinydb import TinyDB
#from tinydb.storages import MemoryStorage

db = TinyDB('data.json', indent=4)
#db = TinyDB(storage=MemoryStorage())
d = {"name": "Patrick", "score": "4"}
db.insert(d)