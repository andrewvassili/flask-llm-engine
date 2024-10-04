# Running Llama3 on AWS using vLLM, Ollama, Llama.cpp (still a work in prog) 

## Model: meta-llama/Meta-Llama-3-8B-Instruct
### Specs:
- Model size: 8B params
- Context window size: 8k (70B model same size)
- https://ai.meta.com/blog/meta-llama-3/

## AWS EC2 machine details:
- Instance type: g5.xlarge
- CPU: 4vCPU
- RAM: 16GB Memory
- Number of GPUs: 1
- GPU type: NVIDIA A10G
- GPU memory: 24GB
- Storage size: 200GB
- CUDA version: 12.2
- Custom AMI: Deep Learning Base (ami-0d576f5cc6a502bb5 64-bit x86)

## Commands to run
```bash
pip install vllm
export HUGGINGFACE_TOKEN=<>
vim vLLM_run.py
```

Then run file [REST_server.py](./platforms/vllm/REST_server.py)

## Testing
### Single requests:
See file [curl_requests.sh](./platforms/vllm/curl_requests.sh)

## Examples of output:
```text 
## Question:
$ curl -X POST http://localhost:8080/generate -H "Content-Type: application/json" -d '{"messages": [{"role": "user", "content": "What is artificial intelligence?"}]}'
## Answer (took 22.4 seconds):
Artificial intelligence (AI) refers to the development of computer systems that can perform tasks that typically require human intelligence, such as:

1. Learning: AI systems can learn from data and improve their performance over time.
2. Problem-solving: AI can analyze complex data, identify patterns, and make decisions or predictions.
3. Reasoning: AI can use logic and rules to draw conclusions and make decisions.
4. Perception: AI can interpret and understand data from sensors, such as images, speech, and text.

There are many types of AI, including:

1. **Machine Learning (ML)**: AI that can learn from data without being explicitly programmed. Examples include speech recognition, image recognition, and natural language processing.
2. **Deep Learning (DL)**: A type of ML that uses neural networks to analyze data. Examples include facial recognition, self-driving cars, and language translation.
3. **Natural Language Processing (NLP)**: AI that can understand, interpret, and generate human language. Examples include chatbots, virtual assistants, and language translation software.
4. **Expert Systems**: AI that mimics human expertise in a specific domain, such as medical diagnosis or financial analysis.
5. **Robotics**: AI that controls physical robots to perform tasks such as assembly, welding, or surgery.
6. **Computer Vision**: AI that can interpret and understand visual data from images and videos.

AI is used in many areas, including:

1. **Healthcare**: Diagnosis, treatment planning, and medical research.
2. **Finance**: Stock market analysis, risk assessment, and portfolio management.
3. **Customer Service**: Chatbots, customer support, and sales.
4. **Transportation**: Autonomous vehicles, traffic management, and route optimization.
5. **Education**: Personalized learning, grading, and adaptive assessment.
6. **Manufacturing**: Quality control, supply chain management, and production planning.

The development of AI has led to many benefits, including:

1. **Increased efficiency**: AI can automate repetitive and mundane tasks, freeing up human resources for more complex tasks.
2. **Improved accuracy**: AI can analyze large amounts of data and make decisions with greater accuracy than humans.
3. **Enhanced customer experience**: AI-powered chatbots and virtual assistants can provide personalized support and services.
4. **New business opportunities**: AI has created new industries and job opportunities, such as AI development, data analysis, and AI consulting.

However, AI also raises concerns about:

1. **Job displacement**: AI may replace certain human jobs, potentially leading to unemployment and social unrest.
2. **Bias and fairness**: AI systems can perpetuate existing biases in data and decision-making.
3. **Privacy**: AI can collect and analyze large amounts of personal data, raising concerns about privacy and security.
4. **Ethical considerations**: AI has the potential to affect human well-being, morals, and values, and requires careful consideration of ethical principles and guidelines.

Overall, AI is a rapidly evolving field with many potential benefits and challenges. As AI becomes more integrated into our daily lives, it is essential to understand its capabilities, limitations, and implications for society.

RequestOutput:
[RequestOutput(request_id=0, prompt='<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n\nWhat is artificial intelligence?<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n', prompt_token_ids=[128000, 128000, 128006, 882, 128007, 271, 3923, 374, 21075, 11478, 30, 128009, 128006, 78191, 128007, 271], prompt_logprobs=None, outputs=[CompletionOutput(index=0, text='Artificial intelligence (AI) refers to the development of computer systems that can perform tasks that typically require human intelligence, such as:\n\n1. Learning: AI systems can learn from data and improve their performance over time.\n2. Problem-solving: AI can analyze complex data, identify patterns, and make decisions or predictions.\n3. Reasoning: AI can use logic and rules to draw conclusions and make decisions.\n4. Perception: AI can interpret and understand data from sensors, such as images, speech, and text.\n\nThere are many types of AI, including:\n\n1. **Machine Learning (ML)**: AI that can learn from data without being explicitly programmed. Examples include speech recognition, image recognition, and natural language processing.\n2. **Deep Learning (DL)**: A type of ML that uses neural networks to analyze data. Examples include facial recognition, self-driving cars, and language translation.\n3. **Natural Language Processing (NLP)**: AI that can understand, interpret, and generate human language. Examples include chatbots, virtual assistants, and language translation software.\n4. **Expert Systems**: AI that mimics human expertise in a specific domain, such as medical diagnosis or financial analysis.\n5. **Robotics**: AI that controls physical robots to perform tasks such as assembly, welding, or surgery.\n6. **Computer Vision**: AI that can interpret and understand visual data from images and videos.\n\nAI is used in many areas, including:\n\n1. **Healthcare**: Diagnosis, treatment planning, and medical research.\n2. **Finance**: Stock market analysis, risk assessment, and portfolio management.\n3. **Customer Service**: Chatbots, customer support, and sales.\n4. **Transportation**: Autonomous vehicles, traffic management, and route optimization.\n5. **Education**: Personalized learning, grading, and adaptive assessment.\n6. **Manufacturing**: Quality control, supply chain management, and production planning.\n\nThe development of AI has led to many benefits, including:\n\n1. **Increased efficiency**: AI can automate repetitive and mundane tasks, freeing up human resources for more complex tasks.\n2. **Improved accuracy**: AI can analyze large amounts of data and make decisions with greater accuracy than humans.\n3. **Enhanced customer experience**: AI-powered chatbots and virtual assistants can provide personalized support and services.\n4. **New business opportunities**: AI has created new industries and job opportunities, such as AI development, data analysis, and AI consulting.\n\nHowever, AI also raises concerns about:\n\n1. **Job displacement**: AI may replace certain human jobs, potentially leading to unemployment and social unrest.\n2. **Bias and fairness**: AI systems can perpetuate existing biases in data and decision-making.\n3. **Privacy**: AI can collect and analyze large amounts of personal data, raising concerns about privacy and security.\n4. **Ethical considerations**: AI has the potential to affect human well-being, morals, and values, and requires careful consideration of ethical principles and guidelines.\n\nOverall, AI is a rapidly evolving field with many potential benefits and challenges. As AI becomes more integrated into our daily lives, it is essential to understand its capabilities, limitations, and implications for society.', token_ids=[9470, 16895, 11478, 320, 15836, 8, 19813, 311, 279, 4500, 315, 6500, 6067, 430, 649, 2804, 9256, 430, 11383, 1397, 3823, 11478, 11, 1778, 439, 1473, 16, 13, 21579, 25, 15592, 6067, 649, 4048, 505, 828, 323, 7417, 872, 5178, 927, 892, 627, 17, 13, 22854, 99246, 25, 15592, 649, 24564, 6485, 828, 11, 10765, 12912, 11, 323, 1304, 11429, 477, 20492, 627, 18, 13, 27857, 287, 25, 15592, 649, 1005, 12496, 323, 5718, 311, 4128, 31342, 323, 1304, 11429, 627, 19, 13, 86950, 25, 15592, 649, 14532, 323, 3619, 828, 505, 26148, 11, 1778, 439, 5448, 11, 8982, 11, 323, 1495, 382, 3947, 527, 1690, 4595, 315, 15592, 11, 2737, 1473, 16, 13, 3146, 22333, 21579, 320, 2735, 33395, 25, 15592, 430, 649, 4048, 505, 828, 2085, 1694, 21650, 56168, 13, 26379, 2997, 8982, 18324, 11, 2217, 18324, 11, 323, 5933, 4221, 8863, 627, 17, 13, 3146, 34564, 21579, 320, 16931, 33395, 25, 362, 955, 315, 20187, 430, 5829, 30828, 14488, 311, 24564, 828, 13, 26379, 2997, 28900, 18324, 11, 659, 60811, 9515, 11, 323, 4221, 14807, 627, 18, 13, 3146, 55381, 11688, 29225, 320, 45, 12852, 33395, 25, 15592, 430, 649, 3619, 11, 14532, 11, 323, 7068, 3823, 4221, 13, 26379, 2997, 6369, 63005, 11, 4200, 57619, 11, 323, 4221, 14807, 3241, 627, 19, 13, 3146, 75392, 15264, 96618, 15592, 430, 28003, 1233, 3823, 19248, 304, 264, 3230, 8106, 11, 1778, 439, 6593, 23842, 477, 6020, 6492, 627, 20, 13, 3146, 44474, 1233, 96618, 15592, 430, 11835, 7106, 29807, 311, 2804, 9256, 1778, 439, 14956, 11, 60022, 11, 477, 15173, 627, 21, 13, 3146, 38432, 31541, 96618, 15592, 430, 649, 14532, 323, 3619, 9302, 828, 505, 5448, 323, 6946, 382, 15836, 374, 1511, 304, 1690, 5789, 11, 2737, 1473, 16, 13, 3146, 14884, 10727, 96618, 95452, 11, 6514, 9293, 11, 323, 6593, 3495, 627, 17, 13, 3146, 79188, 96618, 12937, 3157, 6492, 11, 5326, 15813, 11, 323, 20136, 6373, 627, 18, 13, 3146, 13084, 5475, 96618, 13149, 63005, 11, 6130, 1862, 11, 323, 6763, 627, 19, 13, 3146, 28660, 367, 96618, 97548, 11731, 11, 9629, 6373, 11, 323, 6149, 26329, 627, 20, 13, 3146, 40234, 96618, 19758, 1534, 6975, 11, 66288, 11, 323, 48232, 15813, 627, 21, 13, 3146, 80068, 1711, 96618, 18410, 2585, 11, 8312, 8957, 6373, 11, 323, 5788, 9293, 382, 791, 4500, 315, 15592, 706, 6197, 311, 1690, 7720, 11, 2737, 1473, 16, 13, 3146, 97941, 15374, 96618, 15592, 649, 69711, 59177, 323, 69782, 9256, 11, 67817, 709, 3823, 5070, 369, 810, 6485, 9256, 627, 17, 13, 3146, 82210, 13708, 96618, 15592, 649, 24564, 3544, 15055, 315, 828, 323, 1304, 11429, 449, 7191, 13708, 1109, 12966, 627, 18, 13, 3146, 58568, 4979, 6130, 3217, 96618, 15592, 41503, 6369, 63005, 323, 4200, 57619, 649, 3493, 35649, 1862, 323, 3600, 627, 19, 13, 3146, 3648, 2626, 10708, 96618, 15592, 706, 3549, 502, 19647, 323, 2683, 10708, 11, 1778, 439, 15592, 4500, 11, 828, 6492, 11, 323, 15592, 31831, 382, 11458, 11, 15592, 1101, 25930, 10742, 922, 1473, 16, 13, 3146, 12524, 44153, 96618, 15592, 1253, 8454, 3738, 3823, 7032, 11, 13893, 6522, 311, 26690, 323, 3674, 59322, 627, 17, 13, 3146, 83652, 323, 51841, 96618, 15592, 6067, 649, 22313, 6426, 6484, 50183, 304, 828, 323, 5597, 28846, 627, 18, 13, 3146, 48932, 96618, 15592, 649, 6667, 323, 24564, 3544, 15055, 315, 4443, 828, 11, 19054, 10742, 922, 12625, 323, 4868, 627, 19, 13, 3146, 66490, 950, 38864, 96618, 15592, 706, 279, 4754, 311, 7958, 3823, 1664, 33851, 11, 81436, 11, 323, 2819, 11, 323, 7612, 16994, 18361, 315, 31308, 16565, 323, 17959, 382, 28589, 11, 15592, 374, 264, 19019, 42028, 2115, 449, 1690, 4754, 7720, 323, 11774, 13, 1666, 15592, 9221, 810, 18751, 1139, 1057, 7446, 6439, 11, 433, 374, 7718, 311, 3619, 1202, 17357, 11, 9669, 11, 323, 25127, 369, 8396, 13, 128009], cumulative_logprob=-159.10379307344556, logprobs=None, finish_reason=stop, stop_reason=None)], finished=True, metrics=RequestMetrics(arrival_time=1719654127.4476073, last_token_time=1719654127.4476073, first_scheduled_time=1719654127.4502063, first_token_time=1719654127.556022, time_in_queue=0.002599000930786133, finished_time=1719654149.847301), lora_request=None)]
```

```text
Question:
$ curl -X POST http://localhost:8080/generate -H "Content-Type: application/json" -d '{"messages": [{"role": "user", "content": "What is artificial intelligence? Give me a one sentence answer."}]}'
Answer (took 1.53 seconds):
Artificial intelligence (AI) is the development of computer systems that can perform tasks that would typically require human intelligence, such as learning, problem-solving, and decision-making, through the use of algorithms and data analysis.
```

## Parallel requests script:
```bash
import json
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
```

TODO: Look at AsyncLLMEngine for better performance: https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/api_server.py