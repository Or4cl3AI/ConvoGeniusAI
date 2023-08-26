```python
# convo-genius-ai-studio/backend/models/code_synthesis_model.py

import transformers

class CodeSynthesisModel:
    def __init__(self):
        self.model = transformers.GPT4LMHeadModel()

    def generate_code(self, prompt):
        input_ids = self.model.tokenizer.encode(prompt, return_tensors="pt")
        output = self.model.generate(input_ids, max_length=100, num_return_sequences=1)
        generated_code = self.model.tokenizer.decode(output[0], skip_special_tokens=True)
        return generated_code
```
