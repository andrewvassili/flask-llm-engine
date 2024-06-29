from flask import Flask
from vllm import LLM, SamplingParams
from huggingface_hub import login
import os
from transformers import AutoTokenizer
import logging

app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.INFO)

# Login to Hugging Face
login(os.getenv("HUGGINGFACE_TOKEN"))

# Load the model and tokenizer
logging.info("Loading model...")
model = LLM("meta-llama/Meta-Llama-3-8B-Instruct")
logging.info("Model loaded successfully.")

logging.info("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3-8B-Instruct")
logging.info("Tokenizer loaded successfully.")

sampling_params = SamplingParams(temperature=0.8, top_p=0.95, max_tokens=6000)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    messages = data.get("messages")

    if not messages:
        return jsonify({"error": "No messages provided"}), 400

    formatted_prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    output = model.generate(formatted_prompt, sampling_params)
    print(output)
    # Extract the text from the first output
    if output and output[0].outputs and output[0].outputs[0].text:
        output_text = output[0].outputs[0].text
    else:
        output_text = "No output generated."

    print(output_text)
    return jsonify({"output": output_text}), 200

if __name__ == '__main__':
    logging.info("Starting Flask app...")
    app.run(host='0.0.0.0', port=8080)