import requests
import concurrent.futures
import time
import threading

# Create a lock for thread-safe printing
print_lock = threading.Lock()

def send_request(a, b, iteration):
    url = "http://localhost:8080/completion"
    prompt = f"Answering with just a number, what is {a}+{b}"

    req_json = {
        "stream": False,
        "n_predict": 400,
        "temperature": 0,
        "stop": ["</s>"],
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
    if res.status_code == 200:
        result = res.json()["content"]
        with print_lock:
            print(f"Iteration {iteration}: {result}", flush=True)
    else:
        with print_lock:
            print(f"Iteration {iteration}: Request failed with status code: {res.status_code}", flush=True)

def main():
    start_time = time.time()
    end_time = start_time + 60  # Run for 1 minute
    a = 1
    b = 1
    iteration = 1

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        while time.time() < end_time:
            executor.submit(send_request, a, b, iteration)
            a += 1
            b += 1
            iteration += 1

if __name__ == "__main__":
    main()
