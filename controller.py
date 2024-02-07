from flask import jsonify, request, Flask
from service import CounterService

class CounterController:
    def __init__(self):
        self.counter_service = CounterService()
        self.app = Flask(__name__)
        self.addRoutes()
    
    def addRoutes(self):
        self.app.route('/counters/', methods=['GET'])(self.get_counters)
        self.app.route('/counters', methods=['POST'])(self.create_counter)
        self.app.route('/counters/<counter_name>', methods=['PUT'])(self.increment_counter)
        self.app.route('/counters/<counter_name>', methods=['DELETE'])(self.decrement_counter)
        self.app.route('/counters/<counter_name>', methods=['GET'])(self.get_counter)
    
    def run(self):
        self.app.run(debug=True)

    def get_counters(self):
        return self.counter_service.get_counters()

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
            result = self.counter_service.decrement_counter(counter_name)
            if result:
                return jsonify({"message": f"Counter {counter_name} decremented and deleted"})
            return jsonify({"message": f"Counter {counter_name} decremented"})
        except ValueError as e:
            return jsonify({"error": str(e)}), 404

    def get_counter(self, counter_name: str):
        try:
            return self.counter_service.get_counter(counter_name) 
        except ValueError as e:
            return jsonify({"error": str(e)}), 404