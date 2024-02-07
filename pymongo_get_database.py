from pymongo import MongoClient
def get_database():
   CONNECTION_STRING = "mongodb+srv://dumitruzlotea:3pNWkeGvZ6hz4y%24@cgi-counter-cluster.hty3i7y.mongodb.net/"
 
   client = MongoClient(CONNECTION_STRING)
   return client['cgi-counter']

if __name__ == "__main__":
   dbname = get_database()
