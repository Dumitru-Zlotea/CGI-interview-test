import unittest
from service import CounterService

class TestCounterService(unittest.TestCase):
    def setUp(self):
        self.counter_service = CounterService()
        self.test_counter = {"test": 5}
        self.list_test_counter = ["test", 5]

    def test_get_counters_empty(self):
        self.assertEqual(self.counter_service.get_counters(), [])

    def test_get_counters(self):
        self.counter_service.counters = self.test_counter
        self.assertEqual(self.counter_service.get_counters(), [self.test_counter])

    def test_create_counter(self):
        self.counter_service.create_counter(self.list_test_counter[0], self.list_test_counter[1])
        self.assertEqual(self.counter_service.counters, self.test_counter)

    def test_create_counter_already_exists(self):
        self.counter_service.create_counter(self.list_test_counter[0], self.list_test_counter[1])
        with self.assertRaises(ValueError):
            self.counter_service.create_counter(self.list_test_counter[0], self.list_test_counter[1])

    def test_increment_counter(self):
        self.counter_service.counters = self.test_counter
        self.counter_service.increment_counter(self.list_test_counter[0])
        self.test_counter[self.list_test_counter[0]] += 1
        self.assertEqual(self.counter_service.counters, self.test_counter)

    def test_increment_counter_does_not_exist(self):
        with self.assertRaises(ValueError):
            self.counter_service.increment_counter(self.list_test_counter[0])

    def test_decrement_counter(self):
        self.counter_service.counters = self.test_counter
        self.counter_service.decrement_counter(self.list_test_counter[0])
        self.test_counter[self.list_test_counter[0]] -= 1
        self.assertEqual(self.counter_service.counters, self.test_counter)

    def test_decrement_counter_does_not_exist(self):
        with self.assertRaises(ValueError):
            self.counter_service.decrement_counter(self.list_test_counter[0])

    def test_get_counter(self):
        self.counter_service.counters = self.test_counter
        self.assertEqual(self.counter_service.get_counter(self.list_test_counter[0]), self.test_counter)

    def test_get_counter_does_not_exist(self):
        with self.assertRaises(ValueError):
            self.counter_service.get_counter(self.list_test_counter[0])