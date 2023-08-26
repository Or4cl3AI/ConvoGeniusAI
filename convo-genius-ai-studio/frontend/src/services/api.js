Here is the code for the file `convo-genius-ai-studio/frontend/src/services/api.js`:

```javascript
import axios from 'axios';

const API_URL = 'https://api.convogenius.com';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const fetchConversation = async () => {
  try {
    const response = await api.get('/conversation');
    return response.data;
  } catch (error) {
    console.error('Error fetching conversation:', error);
    throw error;
  }
};

export const sendMessage = async (message) => {
  try {
    const response = await api.post('/message', { message });
    return response.data;
  } catch (error) {
    console.error('Error sending message:', error);
    throw error;
  }
};
```

This code sets up an Axios instance to communicate with the ConvoGenius API. It provides two functions: `fetchConversation` to retrieve the conversation data and `sendMessage` to send a message to the API.