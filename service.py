class CounterService:
    def __init__(self):
        self.counters = {}

    def get_counters(self):
        counters_array = [{key: value} for key, value in self.counters.items()]
        return counters_array

    def create_counter(self, counter_name: str, initial_value: int):
        if counter_name in self.counters:
            raise ValueError(f"Counter with name {counter_name} already exists")
        self.counters[counter_name] = initial_value

    def increment_counter(self, counter_name: str):
        if counter_name not in self.counters:
            raise ValueError(f"Counter with name {counter_name} does not exist")
        self.counters[counter_name] += 1

    # Return True if the counter is deleted, False otherwise
    def decrement_counter(self, counter_name: str):
        if counter_name not in self.counters:
            raise ValueError(f"Counter with name {counter_name} does not exist")
        self.counters[counter_name] -= 1
        if self.counters[counter_name] <= 0:
            del self.counters[counter_name]
            return True
        return False

    def get_counter(self, counter_name: str):
        if counter_name not in self.counters:
            raise ValueError(f"Counter with name {counter_name} does not exist")
        return {counter_name: self.counters[counter_name]}