import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers2"]

# # update 'data' if 'name' exists otherwise insert new document
# mycol.find_one_and_update(
#                           {"session_id": "1234"},
#                           {"$set":{ "chat_history": ["Hello","How are you"]}},
#                          upsert=True)

# print('before update')
# for x in mycol.find():
#   print(x['chat_history'])

# mycol.find_one_and_update(
#                           {"session_id": "1234"},
#                           {"$set":{ "chat_history": ["Hello","How are you", "SAJ!"]}},
#                          upsert=True)

# print('after update')
# for x in mycol.find():
#   print(x['chat_history'])


test = mycol.find_one({"session_id": "1234"})
print(test)
if not test:
    print('empty')
else:
    print('NOT empty')

mycol.delete_one({"session_id": "1234"})