import pymongo
from pymongo import MongoClient

client = MongoClient()

db = client.pymongo_test

posts = db.posts
# post_1 = {
#     'title': 'Python and MongoDB',
#     'content': 'PyMongo is fun, you guys',
#     'author': 'Scott'
# }
# post_2 = {
#     'title': 'Virtual Environments',
#     'content': 'Use virtual environments, you guys',
#     'author': 'Scott'
# }
# post_3 = {
#     'title': 'Learning Python',
#     'content': 'Learn Python, it is easy',
#     'author': 'Bill'
# }
# result = posts.insert_many([post_1,post_2,post_3])
# print('Multiple post: {0}'.format(result.inserted_ids))

bills_post = posts.find({'author': 'Scott'})
for a in bills_post:
    print(a)
