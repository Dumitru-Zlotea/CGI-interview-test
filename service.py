# class CounterService:
#     @staticmethod
#     def __init__():
#         global counters
#         counters = {}

#     @staticmethod
#     def get_counters():
#         return counters

#     @staticmethod
#     def create_counter(counter_name: str, initial_value: int):
#         if counter_name in counters:
#             raise ValueError(f"Counter with name {counter_name} already exists")
#         counters[counter_name] = initial_value

#     @staticmethod
#     def increment_counter(counter_name: str):
#         if counter_name not in counters:
#             raise ValueError(f"Counter with name {counter_name} does not exist")
#         counters[counter_name] += 1

#     @staticmethod
#     def decrement_counter(counter_name: str):
#         if counter_name not in counters:
#             raise ValueError(f"Counter with name {counter_name} does not exist")
#         counters[counter_name] -= 1
#         if counters[counter_name] <= 0:
#             del counters[counter_name]

#     @staticmethod
#     def get_counter(counter_name: str):
#         if counter_name not in counters:
#             raise ValueError(f"Counter with name {counter_name} does not exist")
#         return {counter_name: counters[counter_name]}
class CounterService:
    def __init__(self):
        self.counters = {}

    def get_counters(self):
        return self.counters

    def create_counter(self, counter_name: str, initial_value: int):
        if counter_name in self.counters:
            raise ValueError(f"Counter with name {counter_name} already exists")
        self.counters[counter_name] = initial_value

    def increment_counter(self, counter_name: str):
        if counter_name not in self.counters:
            raise ValueError(f"Counter with name {counter_name} does not exist")
        self.counters[counter_name] += 1

    def decrement_counter(self, counter_name: str):
        if counter_name not in self.counters:
            raise ValueError(f"Counter with name {counter_name} does not exist")
        self.counters[counter_name] -= 1
        if self.counters[counter_name] <= 0:
            del self.counters[counter_name]

    def get_counter(self, counter_name: str):
        if counter_name not in self.counters:
            raise ValueError(f"Counter with name {counter_name} does not exist")
        return {counter_name: self.counters[counter_name]}