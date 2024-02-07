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
    
    def test_get_counters(self):
        self.mock_counter_service.get_counters.return_value = self.test_counter
        response = self.client.get('/counters/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, self.test_counter)
    
    def test_get_counters_empty(self):
        self.mock_counter_service.get_counters.return_value = {}
        response = self.client.get('/counters/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {})
    
    def test_create_counter(self):
        self.mock_counter_service.create_counter.return_value = None
        response = self.client.post('/counters', json={"test": 5})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Counter test created with initial value 5"})

    def test_create_counter_already_exists(self):
        self.mock_counter_service.create_counter.side_effect = ValueError("Counter already exists")
        response = self.client.post('/counters', json={"test": 5})
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.json, {"error": "Counter already exists"})
    
    def test_increment_counter(self):
        self.mock_counter_service.increment_counter.return_value = None
        response = self.client.put(f'/counters/{self.counter_name}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Counter test incremented"})
    
    def test_increment_counter_does_not_exist(self):
           self.mock_counter_service.increment_counter.side_effect = ValueError("Service error")
           response = self.client.put(f'/counters/{self.counter_name}')
           self.assertEqual(response.status_code, 404)
           self.assertEqual(response.json, {"error": "Service error"})
        
    def test_decrement_counter(self):
        self.mock_counter_service.decrement_counter.return_value = False
        response = self.client.delete(f'/counters/{self.counter_name}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Counter test decremented"})
    
    def test_decrement_counter_delete(self):
        self.mock_counter_service.decrement_counter.return_value = True
        response = self.client.delete(f'/counters/{self.counter_name}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Counter test decremented and deleted"})
    
    def test_decrement_counter_does_not_exist(self):
        self.mock_counter_service.decrement_counter.side_effect = ValueError("Service error")
        response = self.client.delete(f'/counters/{self.counter_name}')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {"error": "Service error"})
    
    def test_get_counter(self):
        self.mock_counter_service.get_counter.return_value = self.test_counter
        response = self.client.get(f'/counters/{self.counter_name}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, self.test_counter)
    
    def test_get_counter_does_not_exist(self):
        self.mock_counter_service.get_counter.side_effect = ValueError("Service error")
        response = self.client.get(f'/counters/{self.counter_name}')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {"error": "Service error"})
