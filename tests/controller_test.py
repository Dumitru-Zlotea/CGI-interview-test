import unittest
from controller import CounterController
from app import app
from flask import jsonify

class TestCounterController(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.context = app.app_context()
        self.context.push()
        self.counter_controller = CounterController()
        self.test_counter = {"test": 5}
        self.counter_name = "test"
        self.counter_value = 5
        self.conflict_status_code = 409

    def tearDown(self):
        self.context.pop()

    def test_get_counters(self):
        self.counter_controller.counter_service.counters = self.test_counter
        response = self.counter_controller.get_counters()
        self.assertEqual(response.data, jsonify(self.test_counter).data)

    def test_create_counter(self):
        response = self.app.post('/counters', json={self.counter_name: self.counter_value})
        self.assertEqual(response.data, jsonify({"message": f"Counter {self.counter_name} created with initial value {self.counter_value}"}).data)

    def test_create_counter_already_exists(self):
        self.counter_controller.counter_service.counters = self.test_counter
        response = self.app.post('/counters', json={self.counter_name: self.counter_value})
        self.assertEqual(response.status_code, self.conflict_status_code)
        self.assertEqual(response.data, jsonify({"error": f"Counter with name {self.counter_name} already exists"}).data)

    def test_increment_counter(self):
        self.counter_controller.counter_service.counters = self.test_counter
        self.counter_controller.increment_counter(self.counter_name)
        self.test_counter[self.counter_name] += 1
        self.assertEqual(self.counter_controller.counter_service.counters, self.test_counter)

# tests work until here
    # def test_increment_counter_does_not_exist(self):
    #     self.counter_controller.counter_service.counters = {}
    #     response = self.app.put(f'/counters/{self.counter_name}')
    #     #self.assertEqual(response.status_code, 404)
    #     self.assertEqual(response.data, jsonify({"error": f"Counter with name {self.counter_name} does not exist"}).data)

    # def test_increment_counter_does_not_exist(self):
    #     with self.assertRaises(ValueError):
    #         self.counter_controller.increment_counter(self.counter_name)

    # def test_decrement_counter(self):
    #     self.counter_controller.decrement_counter(self.counter_name)
    #     self.test_counter[self.counter_name] -= 1
    #     self.assertEqual(self.counter_controller.get_counters(), self.test_counter)

    # def test_decrement_counter_does_not_exist(self):
    #     with self.assertRaises(ValueError):
    #         self.counter_controller.decrement_counter(self.counter_name)

    # def test_get_counter(self):
    #     self.assertEqual(self.counter_controller.get_counter(self.counter_name), self.test_counter)

    # def test_get_counter_does_not_exist(self):
    #     with self.assertRaises(ValueError):
    #         self.counter_controller.get_counter(self.counter_name)