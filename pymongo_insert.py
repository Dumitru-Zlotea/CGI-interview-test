# I'm keeping this file for test purposes to quickly insert data into the database.
# To run this file, simply run the following command in the terminal: python pymongo_insert.py

from pymongo_get_database import get_database

dbname = get_database()
collection = dbname['cgi-counter']

counter1 = {"counter1": 3}
counter2 = {"counter2": 13}

collection.insert_many([counter1, counter2])
