```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to ConvoGenius AI Studio: Crafting Conversations, Code, and Dreams'

if __name__ == '__main__':
    app.run()
```