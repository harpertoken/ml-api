---
license: mit
language:
- en
base_model:
- bniladridas/conversational-ai-base-model
tags:
- text-generation-inference
- conversational-ai
- gpt2
metrics:
- perplexity
- bleu
- f1
library_name: transformers
---

![Hugging Face Logo](https://huggingface.co/front/assets/huggingface_logo-noborder.svg)

# Conversational AI Fine-Tuned Model

## Model Details
- **Model Name**: Conversational AI Fine-Tuned Model
- **Base Model**: bniladridas/conversational-ai-base-model
- **Model Type**: GPT-2-based conversational AI model
- **Max Sequence Length**: 256 tokens

## Intended Use
This model is designed to generate human-like responses for conversational applications, such as chatbots, virtual assistants, and dialogue systems.

## Training Data
The model was fine-tuned on the DailyDialog dataset, featuring:
- **Training Examples**: 11,118
- **Validation Examples**: 1,000
- **Test Examples**: 1,000

## Dataset Characteristics
- **Description**: A high-quality, multi-turn dialogue dataset covering everyday topics.
- **Features**: Includes dialogues, communication acts, and emotion annotations.
- **Citation**:
  ```
  @InProceedings{li2017dailydialog,
      author = {Li, Yanran and Su, Hui and Shen, Xiaoyu and Li, Wenjie and Cao, Ziqiang and Niu, Shuzi},
      title = {DailyDialog: A Manually Labelled Multi-turn Dialogue Dataset},
      booktitle = {Proceedings of The 8th International Joint Conference on Natural Language Processing (IJCNLP 2017)},
      year = {2017}
  }
  ```

## Training Configuration
- **Learning Rate**: 2e-5
- **Batch Size**: 8 (for both training and evaluation)
- **Number of Epochs**: 3
- **Weight Decay**: 0.01

## Ethical Considerations
Inherited from the GPT-2 base model and the DailyDialog dataset, this model may reflect biases or limitations present in its training data. Caution is advised when using it in sensitive contexts, as it could produce biased or inappropriate responses.

## How to Use

### Using the Model Directly
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load model and tokenizer
model = AutoModelForCausalLM.from_pretrained("bniladridas/conversational-ai-fine-tuned")
tokenizer = AutoTokenizer.from_pretrained("bniladridas/conversational-ai-fine-tuned")

# Prepare input
input_text = "Hello, how are you?"
inputs = tokenizer(input_text, return_tensors="pt")

# Generate response
outputs = model.generate(**inputs)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)
```

### Using the Terminal
Run the provided script to generate responses:
```bash
python3 generate_response.py --input "Hello, how are you?"
```

### Using the API
**Check API Status:**
```bash
curl http://localhost:8000/status
```

**Generate a Response:**
```bash
curl -X POST http://localhost:8000/chat -H "Content-Type: application/json" -d '{"input_text": "Hello, how are you?"}'
```

### Using FastAPI Documentation
Interact with the API via the browser at:
[http://localhost:8000/docs#/default/generate_response_chat_post](http://localhost:8000/docs#/default/generate_response_chat_post)

## Test Cases
The following tests were conducted to validate the model:

### Terminal Script Test:
```bash
python3 generate_response.py --input "Hello, how are you?"
```
**Output:**
```
Hello how are you?   Fine thanks.   How are you?
```

### API Status Check:
```bash
curl http://localhost:8000/status
```
**Output:**
```json
{"status": "API is running"}
```

### API Chat Response:
```bash
curl -X POST http://localhost:8000/chat -H "Content-Type: application/json" -d '{"input_text": "Hello, how are you?"}'
```
**Output:**
```json
{"response": "Hello how are you?   Fine thanks.   How are you?"}
```

## Example Usage
*Example interactions are not yet provided. Users can test the model with their own inputs using the methods above to see its conversational capabilities.*