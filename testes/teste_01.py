teste01
import unittest

class TestWebsiteAccessibility(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

    def test_website_accessibility(self):
        self.driver.get('https://www.example.com')
        self.assertIn('Example Domain', self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

