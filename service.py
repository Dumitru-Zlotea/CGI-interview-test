from pymongo_get_database import get_database

class CounterService:
    def __init__(self):
        self.dbname = get_database()
        self.collection = self.dbname['cgi-counter']
        self.projection = {"_id": 0}

    def get_counters(self):
        counters = self.collection.find(projection=self.projection)
        counters_array = []
        for document in counters:
            counters_array.append(document)
        return counters_array

    def create_counter(self, counter_name: str, initial_value: int):
        if self.collection.find_one({counter_name: {"$exists": True}}, projection=self.projection):
            raise ValueError(f"Counter with name {counter_name} already exists")
        self.collection.insert_one({counter_name: initial_value})

    def increment_counter(self, counter_name: str):
        if not self.collection.find_one({counter_name: {"$exists": True}}, projection=self.projection):
            raise ValueError(f"Counter with name {counter_name} does not exist")
        self.collection.update_one({counter_name: {"$exists": True}}, {"$inc": {counter_name: 1}})

    # Return True if the counter is deleted, False otherwise
    def decrement_counter(self, counter_name: str):
        if not self.collection.find_one({counter_name: {"$exists": True}}, projection=self.projection):
            raise ValueError(f"Counter with name {counter_name} does not exist")
        self.collection.update_one({counter_name: {"$exists": True}}, {"$inc": {counter_name: -1}})
        counter = self.collection.find_one({counter_name: {"$exists": True}}, projection=self.projection)
        if counter[counter_name] <= 0:
            self.collection.delete_one({counter_name: {"$exists": True}})
            return True
        return False

    def get_counter(self, counter_name: str):
        counter = self.collection.find_one({counter_name: {"$exists": True}}, projection=self.projection)
        if not counter:
            raise ValueError(f"Counter with name {counter_name} does not exist")
        return counter