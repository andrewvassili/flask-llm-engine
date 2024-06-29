from concurrent.futures import ThreadPoolExecutor, as_completed

# List of questions to test the server
questions = [
    "What is the capital of Australia?",
    "When did the First World War begin?",
    "Who was Albert Einstein?",
    "What is the speed of light?",
    "What is blockchain technology?",
    "What are the largest deserts in the world?",
    "Who wrote the play Hamlet?",
    "What is photosynthesis?",
    "What is the Pythagorean theorem?",
    "Who won the FIFA World Cup in 2018?",
    "What is a black hole?",
    "Who was the first President of the United States?",
    "What is inflation?",
    "Who composed the Symphony No. 9?",
    "What is Impressionism?",
    "What is the function of the liver?",
    "What is existentialism?",
    "What is democracy?",
    "What is artificial intelligence?",
    "What is climate change?"
]

# URL of the REST endpoint
url = "http://localhost:8080/generate"

# Function to send a POST request
def send_request(question):
    payload = {
        "messages": [{"role": "user", "content": question}]
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return question, response.json()

# Main function to run the script
def main():
    with ThreadPoolExecutor(max_workers=5) as executor:  # Adjust max_workers as needed
        futures = [executor.submit(send_request, question) for question in questions]
        for future in as_completed(futures):
            question, response = future.result()
            print(f"Question: {question}")
            print("Response:", response)

if __name__ == "__main__":
    main()