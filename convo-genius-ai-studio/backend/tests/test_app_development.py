```python
import unittest
from app.api.app_development import create_app, deploy_app, update_app, delete_app

class TestAppDevelopment(unittest.TestCase):
    def setUp(self):
        self.app = create_app("MyApp")
    
    def test_create_app(self):
        self.assertEqual(self.app.name, "MyApp")
    
    def test_deploy_app(self):
        self.assertEqual(deploy_app(self.app), "App deployed successfully")
    
    def test_update_app(self):
        self.assertEqual(update_app(self.app, "NewApp"), "App updated successfully")
    
    def test_delete_app(self):
        self.assertEqual(delete_app(self.app), "App deleted successfully")

if __name__ == '__main__':
    unittest.main()
```