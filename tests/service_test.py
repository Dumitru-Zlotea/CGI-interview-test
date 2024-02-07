import unittest
from service import CounterService
from mock import patch

class TestCounterService(unittest.TestCase):
    @patch('service.get_database')
    def setUp(self, Mockget_database):
        self.mock_database = Mockget_database.return_value
        self.mock_collection = self.mock_database['cgi-counter']
        self.counter_service = CounterService()
        self.test_counter = {"test": 5}

    def test_get_counters(self):
        self.mock_collection.find.return_value = [self.test_counter]
        response = self.counter_service.get_counters()
        self.assertEqual(response[0], self.test_counter)

    def test_get_counters_empty(self):
        self.mock_collection.find.return_value = []
        response = self.counter_service.get_counters()
        self.assertEqual(response, [])
    
    def test_create_counter(self):
        self.mock_collection.find_one.return_value = None
        self.counter_service.create_counter("test", 5)
        self.mock_collection.insert_one.assert_called_once_with({"test": 5})

    def test_create_counter_already_exists(self):
        self.mock_collection.find_one.return_value = {"test": 5}
        with self.assertRaises(ValueError) as e:
            self.counter_service.create_counter("test", 5)
        self.assertEqual(str(e.exception), "Counter with name test already exists")
    
    def test_increment_counter(self):
        self.mock_collection.find_one.return_value = {"test": 5}
        self.counter_service.increment_counter("test")
        self.mock_collection.update_one.assert_called_once_with({"test": {"$exists": True}}, {"$inc": {"test": 1}})

    def test_increment_counter_does_not_exist(self):
        self.mock_collection.find_one.return_value = None
        with self.assertRaises(ValueError) as e:
            self.counter_service.increment_counter("test")
        self.assertEqual(str(e.exception), "Counter with name test does not exist")

    def test_decrement_counter(self):
        self.mock_collection.find_one.return_value = {"test": 5}
        self.mock_collection.find_one.return_value = {"test": 4}
        response = self.counter_service.decrement_counter("test")
        self.assertEqual(response, False)

    def test_decrement_counter_delete(self):
        self.mock_collection.find_one.return_value = {"test": 0}
        self.counter_service.decrement_counter("test")
        self.mock_collection.delete_one.assert_called_once_with({"test": {"$exists": True}})

    def test_decrement_counter_does_not_exist(self):
        self.mock_collection.find_one.return_value = None
        with self.assertRaises(ValueError) as e:
            self.counter_service.decrement_counter("test")
        self.assertEqual(str(e.exception), "Counter with name test does not exist")

    def test_get_counter(self):
        self.mock_collection.find_one.return_value = {"test": 5}
        response = self.counter_service.get_counter("test")
        self.assertEqual(response, {"test": 5})
    
    def test_get_counter_does_not_exist(self):
        self.mock_collection.find_one.return_value = None
        with self.assertRaises(ValueError) as e:
            self.counter_service.get_counter("test")
        self.assertEqual(str(e.exception), "Counter with name test does not exist")
    