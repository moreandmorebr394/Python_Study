import pymongo as pyM
import datetime
import pprint

client = pyM.MongoClient()

db = client.test 
collection = db.test_collection
print(db.list_collection

#definição de infor para compor o file

post = {
  "autor":"Mike",
  "text":"My first mongodb application based on python",
  "tags":"["mongodb, "python3", "pymongo"],
  "date": datetime.datetime.utcnow()
}

posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)

print(db.posts)

# print(db.posts.find_one())

pprint.pprint(db.posts.find_one))

#bulk inserts
new_posts = [{
  "author":"Mike",
  "text":"Another post",
  "tags": ["bulk", "post", "insert"],
  "date": datetimr.datetime.utcnow()
}
{ 
  "author":"Joao",
  "text":"Post from Joao. New post available",
  "title": "Mongo is fun",
  "date": datetimr.datetime.utcnow(2003, 11, 10, 10, 45)

}]

result = posts.insert_many(new_posts)
print(result.inserted_id)

print("\nRecuperação final")
pprint.pprint(db.posts.find_one())

print("\n Documentos presentes na coleção posts")
for post in posts.find():
  pprint.pprint(post)
