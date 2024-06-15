import logging

import ollama
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins='*')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

MODEL_NAME = 'tinyllama'
ollama_client = ollama.Client()
ollama.pull(MODEL_NAME)


@app.route('/generate-topic', methods=['POST'])
def generate_topic():
    try:
        prompt = request.json.get('prompt')
        logging.info(prompt)
        if not prompt:
            return jsonify({'error': 'No prompt provided'}), 400

        response = ollama.chat(
            model=MODEL_NAME,
            messages=[{'role': 'user', 'content': f'Create a 3-5 word topic title using the following as context: {prompt}'}],
            # stream=True
        )
        # for chunk in stream:
        #     print(chunk['messages']['content'], end='', flush=True)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
