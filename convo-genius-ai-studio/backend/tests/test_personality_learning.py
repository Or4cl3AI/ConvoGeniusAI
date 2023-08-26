```python
import unittest
from backend.models.context_management import Personality

class PersonalityLearningTest(unittest.TestCase):
    def test_personality_learning(self):
        personality = Personality()
        personality.learn("Hello, how are you?")
        self.assertEqual(personality.generate_response(), "I'm doing well, thank you!")

if __name__ == '__main__':
    unittest.main()
```
