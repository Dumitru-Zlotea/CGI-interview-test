import unittest
from flask.json import jsonify
from mock import patch
from controller import CounterController

class TestCounterController(unittest.TestCase):
    @patch('controller.CounterService')
    def setUp(self, MockCounterService):
        self.mock_counter_service = MockCounterService.return_value
        self.counter_controller = CounterController()
        self.counter_controller.app.testing = True
        self.client = self.counter_controller.app.test_client()
        self.test_counter = {"test": 5}
        self.counter_name = "test"
        self.counter_value = 5
        
        self.context = self.counter_controller.app.app_context()
        self.context.push()

    def tearDown(self):
        self.context.pop()

    def test_increment_counter_does_not_exist(self):
           self.mock_counter_service.increment_counter.side_effect = ValueError("Service error")
           response = self.client.put(f'/counters/{self.counter_name}')
           self.assertEqual(response.status_code, 404)
           self.assertEqual(response.json, {"error": "Service error"})

