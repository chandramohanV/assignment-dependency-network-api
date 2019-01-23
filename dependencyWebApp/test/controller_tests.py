from app import controller
import unittest

class controller_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        # creates a test client
        self.app = controller.app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def tearDown(self):
        pass

    def test_heartbeat_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/api')
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_heartbeat_data(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/api')

        # assert the response data
        self.assertEqual(result.data, b'Alive')
