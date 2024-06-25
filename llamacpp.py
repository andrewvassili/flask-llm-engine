# https://medium.com/vendi-ai/efficiently-run-your-fine-tuned-llm-locally-using-llama-cpp-66e2a7c51300
# git clone git@github.com:ggerganov/llama.cpp.git
# cd llama.cpp
# make
# <download quantized gguf model from hf>
# ./llama-server -m ~/Downloads/<model> --> runs on localhost:8080


def main():
    import requests

    url = f"http://localhost:8080/completion"
    prompt = "Hi there"

    req_json = {
        "stream": False,
        "n_predict": 400,
        "temperature": 0,
        "stop": [
            "</s>",
        ],
        "repeat_last_n": 256,
        "repeat_penalty": 1,
        "top_k": 20,
        "top_p": 0.75,
        "tfs_z": 1,
        "typical_p": 1,
        "presence_penalty": 0,
        "frequency_penalty": 0,
        "mirostat": 0,
        "mirostat_tau": 5,
        "mirostat_eta": 0.1,
        "grammar": "",
        "n_probs": 0,
        "prompt": prompt
    }

    res = requests.post(url, json=req_json)
    result = res.json()["content"]
    print(result)

if __name__ == '__main__':
    main()