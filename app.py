from flask import Flask
from controller import CounterController

app = Flask(__name__)

counter_controller = CounterController()

app.route('/counters/', methods=['GET'])(counter_controller.get_counters)
app.route('/counters', methods=['POST'])(counter_controller.create_counter)
app.route('/counters/<counter_name>', methods=['PUT'])(counter_controller.increment_counter)
app.route('/counters/<counter_name>', methods=['DELETE'])(counter_controller.decrement_counter)
app.route('/counters/<counter_name>', methods=['GET'])(counter_controller.get_counter)

if __name__ == '__main__':
    app.run(debug=True)
