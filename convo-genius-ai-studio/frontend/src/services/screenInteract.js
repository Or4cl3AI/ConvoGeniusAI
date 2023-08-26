Here is the code for the file `convo-genius-ai-studio/frontend/src/services/screenInteract.js`:

```javascript
import axios from 'axios';
import { openCV, tensorflow, pyAutoGUI } from '../../backend/utils/computer_vision';

const screenInteract = {
  captureScreenshot: async () => {
    try {
      const response = await axios.get('/api/screen_interaction/capture_screenshot');
      return response.data;
    } catch (error) {
      console.error('Error capturing screenshot:', error);
      throw error;
    }
  },

  performOCR: async (image) => {
    try {
      const response = await axios.post('/api/screen_interaction/perform_ocr', { image });
      return response.data;
    } catch (error) {
      console.error('Error performing OCR:', error);
      throw error;
    }
  },

  locateObject: async (objectName) => {
    try {
      const response = await axios.post('/api/screen_interaction/locate_object', { objectName });
      return response.data;
    } catch (error) {
      console.error('Error locating object:', error);
      throw error;
    }
  },

  clickOnObject: async (objectName) => {
    try {
      const response = await axios.post('/api/screen_interaction/click_on_object', { objectName });
      return response.data;
    } catch (error) {
      console.error('Error clicking on object:', error);
      throw error;
    }
  },

  typeOnObject: async (objectName, text) => {
    try {
      const response = await axios.post('/api/screen_interaction/type_on_object', { objectName, text });
      return response.data;
    } catch (error) {
      console.error('Error typing on object:', error);
      throw error;
    }
  },

  performGesture: async (gesture) => {
    try {
      const response = await axios.post('/api/screen_interaction/perform_gesture', { gesture });
      return response.data;
    } catch (error) {
      console.error('Error performing gesture:', error);
      throw error;
    }
  },

  applyFilter: async (image, filter) => {
    try {
      const response = await axios.post('/api/screen_interaction/apply_filter', { image, filter });
      return response.data;
    } catch (error) {
      console.error('Error applying filter:', error);
      throw error;
    }
  },

  processImage: async (image) => {
    try {
      const response = await axios.post('/api/screen_interaction/process_image', { image });
      return response.data;
    } catch (error) {
      console.error('Error processing image:', error);
      throw error;
    }
  },

  performObjectDetection: async (image) => {
    try {
      const response = await axios.post('/api/screen_interaction/perform_object_detection', { image });
      return response.data;
    } catch (error) {
      console.error('Error performing object detection:', error);
      throw error;
    }
  },

  applyStyleTransfer: async (contentImage, styleImage) => {
    try {
      const response = await axios.post('/api/screen_interaction/apply_style_transfer', { contentImage, styleImage });
      return response.data;
    } catch (error) {
      console.error('Error applying style transfer:', error);
      throw error;
    }
  },

  performScreenRecognition: async () => {
    try {
      const response = await axios.get('/api/screen_interaction/perform_screen_recognition');
      return response.data;
    } catch (error) {
      console.error('Error performing screen recognition:', error);
      throw error;
    }
  },

  performScreenInteraction: async () => {
    try {
      const response = await axios.get('/api/screen_interaction/perform_screen_interaction');
      return response.data;
    } catch (error) {
      console.error('Error performing screen interaction:', error);
      throw error;
    }
  },
};

export default screenInteract;
```

Please note that this code assumes the existence of the following dependencies:

- `axios` for making HTTP requests
- `openCV`, `tensorflow`, and `pyAutoGUI` from the `../../backend/utils/computer_vision` module

Make sure to install these dependencies and adjust the import paths accordingly.