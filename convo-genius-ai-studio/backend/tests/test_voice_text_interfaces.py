```python
import unittest
from app.api.voice_text_interfaces import VoiceTextInterfaces

class TestVoiceTextInterfaces(unittest.TestCase):
    def setUp(self):
        self.voice_text = VoiceTextInterfaces()

    def test_convert_text_to_speech(self):
        text = "Hello, ConvoGenius!"
        result = self.voice_text.convert_text_to_speech(text)
        self.assertEqual(result, "Speech generated successfully.")

    def test_transcribe_speech(self):
        audio_file = "audio.wav"
        result = self.voice_text.transcribe_speech(audio_file)
        self.assertEqual(result, "Speech transcribed successfully.")

    def test_recognize_speech(self):
        audio_file = "audio.wav"
        result = self.voice_text.recognize_speech(audio_file)
        self.assertEqual(result, "Speech recognized successfully.")

if __name__ == "__main__":
    unittest.main()
```
