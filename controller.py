from flask import jsonify, request
from service import CounterService

class CounterController:
    def __init__(self):
        self.counter_service = CounterService()

    def get_counters(self):
        counters = self.counter_service.get_counters()
        return jsonify(counters)
    
    def create_counter(self):
        data = request.get_json()
        counter_name, initial_value = data.popitem()
        try:
            self.counter_service.create_counter(counter_name, initial_value)
            return jsonify({"message": f"Counter {counter_name} created with initial value {initial_value}"})
        except ValueError as e:
            return jsonify({"error": str(e)}), 409
        
    def increment_counter(self, counter_name: str):
        try:
            self.counter_service.increment_counter(counter_name)
            return jsonify({"message": f"Counter {counter_name} incremented"})
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        
    def decrement_counter(self, counter_name: str):
        try:
            self.counter_service.decrement_counter(counter_name)
            return jsonify({"message": f"Counter {counter_name} decremented"})
        except ValueError as e:
            return jsonify({"error": str(e)}), 404

    def get_counter(self, counter_name: str):
        try:
            counter = self.counter_service.get_counter(counter_name)
            return jsonify(counter)
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
    