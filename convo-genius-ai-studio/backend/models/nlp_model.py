```python
import transformers

class NLPModel:
    def __init__(self):
        self.tokenizer = transformers.AutoTokenizer.from_pretrained("gpt-4")
        self.model = transformers.AutoModelForCausalLM.from_pretrained("gpt-4")

    def generate_text(self, prompt):
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt")
        output = self.model.generate(input_ids, max_length=100, num_return_sequences=1)
        generated_text = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return generated_text
```
