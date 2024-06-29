# https://medium.com/vendi-ai/efficiently-run-your-fine-tuned-llm-locally-using-llama-cpp-66e2a7c51300
# git clone git@github.com:ggerganov/llama.cpp.git
# cd llama.cpp
# make
# <download quantized gguf model from hf>
# ./llama-server -m ~/Downloads/<model> --> runs on localhost:8080


# On EC2:
# sudo yum update -y
# sudo yum install git -y
# git --version

# ssh-keygen -t ed25519 -C "your_email@example.com"
# eval "$(ssh-agent -s)"
# ssh-add ~/.ssh/id_ed25519
# cat ~/.ssh/id_ed25519.pub
# create SSH key in GitHub with pub key from ^

# git clone git@github.com:ggerganov/llama.cpp.git
# cd llama.cpp
# sudo yum install make -y
# sudo yum groupinstall 'Development Tools' -y


# make
# <download quantized gguf model from hf>
# ./llama-server -m ~/Downloads/<model> --> runs on localhost:8080
# ./llama-server -m ~/Downloads/<model> --> runs on localhost:8080 --server --parallel 2 --cont-batching
    # TODO: check out https://github.com/ggerganov/llama.cpp/tree/master/examples/server


# Convert pytorch model to gguf: https://github.com/OpenBMB/llama.cpp/tree/minicpm-v2.5/examples/minicpmv


def main():
    import requests

    url = f"http://localhost:8080/completion"
    prompt = "What colour is the sky?"

    req_json = {
        "stream": False,
        "n_predict": 400,
        "temperature": 0,
        # "stop": [
        #     "</s>",
        # ],
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