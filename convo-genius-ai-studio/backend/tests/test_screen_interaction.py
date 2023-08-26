```python
import unittest
from convo_genius_ai_studio.backend.app.api.screen_interaction import *

class TestScreenInteraction(unittest.TestCase):
    def test_capture_screenshot(self):
        # Test capturing a screenshot
        screenshot_path = capture_screenshot()
        self.assertTrue(os.path.exists(screenshot_path))

    def test_extract_text_from_image(self):
        # Test extracting text from an image
        image_path = "path/to/image.png"
        extracted_text = extract_text_from_image(image_path)
        self.assertEqual(extracted_text, "Hello, World!")

    def test_perform_screen_interaction(self):
        # Test performing screen interaction
        interaction_result = perform_screen_interaction()
        self.assertTrue(interaction_result)

if __name__ == "__main__":
    unittest.main()
```
