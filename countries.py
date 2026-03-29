from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["countries"]
collection = db["countries"]

##docs = collection.find()

#for doc in docs:
#	print(doc)
	
##doc = collection.find_one()


#for doc in collection.find({"name": {"$regex": "^A"}}):
#	print(doc)

#for doc in collection.find({"code": "AR"}):
#	print(doc)
	
#for doc in collection.find({"region": "Europe"}):
#	print(doc)

#for doc in collection.find({"currency": "RUB"}):
#	print(doc)

#for doc in collection.find({
#	"capital": {"$regex": "^C"}
#}):
#	print(doc)

#collection.update_one(
#	{"code": "AR"},
#	{"$set": {"currency": "USD"}
 # }
#)

#doc = collection.find_one({"code": "AR"})
#print(doc)

#collection.update_one(
#	{"name": "Belgium"},{"$inc": {"population": 1000000}}
##)
#doc = collection.find_one({"name": "Belgium"})
#print(doc)


#collection.update_one(
#	{"code": "BR"}, {"$set": {"capital": "Rio de Janeiro"}}
#)

#doc = collection.find_one({"name": "Brazil"})
#print(doc)


#collection.update_many(
#	{"region": "Americas"},{"$set": {"region": "America"}}
#)

#docs = collection.find({"region": "America"})
#for doc in docs:
 # 
 #   print(doc)

collection.delete_many({"name": {"$regex": "^B"}})