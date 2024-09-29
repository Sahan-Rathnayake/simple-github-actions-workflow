import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from app import app

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        """Test home page load and contents."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Enter Your Name', response.data)
        self.assertIn(b'<input', response.data)
        self.assertIn(b'<button', response.data)

    def test_greeting_page(self):
        """Test greeting functionality."""
        response = self.app.post('/', data={'username': 'Sahan'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, Nikila', response.data)
        self.assertIn(b'Welcome to GitHub Actions Demo', response.data)
        self.assertIn(b'<button class="go-back">Go Back</button>', response.data)

    def test_go_back_button(self):
        """Test Back button functionality."""
        response = self.app.post('/', data={'username': 'Sahan'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, Sahan', response.data)
        self.assertIn(b'Welcome to GitHub Actions Demo', response.data)
        
        self.assertIn(b'<button class="go-back">Go Back</button>', response.data)

        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Enter Your Name', response.data)

if __name__ == '__main__':
    unittest.main()
