from pymongo import MongoClient


def connect_db():
    client = MongoClient('mongodb://mongouser:mongouser123@cluster0-shard-00-00.vljyz.mongodb.net:27017,'
                         'cluster0-shard-00-01.vljyz.mongodb.net:27017,cluster0-shard-00-02.vljyz.mongodb.net:'
                         '27017/crawling?ssl=true&replicaSet=atlas-vildf2-shard-0&authSource=admin&retryWrites='
                         'true&w=majority')
    db = client['crawling']
    db = db['crawling_collection']
    return db


def post_feed(db_collection, post_collection, guid):
    try:
        db_collection.insert_one(post_collection).inserted_id
        print(guid+': inserido no banco de dados!')

    except Exception as e:
        print(e)

def list_feed(db_collection):
    cursor = db_collection.find({})
    for document in cursor:
        print(document)