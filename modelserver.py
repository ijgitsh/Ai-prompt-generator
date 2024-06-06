from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import config

app = Flask(__name__)
CORS(app)

def get_credentials():
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
    }
    data = {
        'grant_type': 'urn:ibm:params:oauth:grant-type:apikey',
        'apikey': config.CLOUD_API_KEY,
    }
    # Use the requests library to make the HTTP request
    response = requests.post(config.AUTH_URL, headers=headers, data=data, verify=False)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        json_data = response.json()

        # Access the token from the JSON data
        access_token = json_data.get('access_token', None)

        if access_token:
            print(f'The access token is: {access_token}')
        else:
            print('Access token not found in the JSON response.')
    else:
        print(f'Request failed with status code: {response.status_code}')
        print(f'Response content: {response.text}')

    return access_token

def invoke_prompt(access_token):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    response = requests.get(config.PROMPT_URL, headers=headers)

    if response.status_code == 200:
        generated_text = response.json()
        if generated_text:
            resources = generated_text.get("resources", [])
            model_ids = [model.get("model_id") for model in resources]
            return model_ids
        else:
            return []
    else:
        print(f'Request failed with status code: {response.status_code}')
        print(f'Response content: {response.text}')
        return []

@app.route('/models', methods=['GET'])
def get_models():
    access_token = get_credentials()
    models = invoke_prompt(access_token)
    return jsonify(models)

@app.route('/getprompts', methods=['POST'])
def get_prompts():
    data = request.get_json()
    models = data.get('models', [])
    text = data.get('text', '')
    access_token = get_credentials()
    print("Received models:", models)
    print("Received text:", text)

    results = []
    for modelType in models:
        print("getting prompt for " + modelType)
        post_data = {
            "input": (
                "context: You are an expert in artificial intelligence and prompt engineering. Your task is to create a comprehensive and detailed prompt for an AI system to generate high-quality responses. The prompt should include specific instructions, context, and examples to ensure the AI understands the task and produces accurate, relevant, and concise answers.\n"

                "Instructions:\n"
                "1. Provide a detailed background of the topic or task.\n"
                "2. Clearly outline the structure and format of the desired response.\n"
                "3. Include specific questions or points the AI should address in its response.\n"
                "4. Provide examples of high-quality responses for reference.\n"
                "5. Emphasize the importance of accuracy, relevance, and conciseness in the response.\n"
                "6. Ensure the prompt is easy to understand and follow.\n"
                f"generate a prompt for this subject: \n{text}"
            ),
            "parameters": {
                "decoding_method": "greedy",
                "max_new_tokens": 1000,
                "min_new_tokens": 0,
                "stop_sequences": [],
                "repetition_penalty": 1
            },
            "model_id": modelType,
            "project_id": config.PROJECT_ID,
            "moderations": {
                "hap": {
                    "input": {
                        "enabled": True,
                        "threshold": 0.5,
                        "mask": {
                            "remove_entity_value": True
                        }
                    },
                    "output": {
                        "enabled": True,
                        "threshold": 0.5,
                        "mask": {
                            "remove_entity_value": True
                        }
                    }
                }
            }
        }

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {access_token}",
        }
        response = requests.post(
            config.GENERATE_URL,
            headers=headers,
            json=post_data
        )
        generated_text = "This model does not support this function"
        if response.status_code != 200:
            print("error generating for " + modelType)
            results.append({"model": modelType, "generated_text": "does not support"})
        else:
            response_data = response.json()
            print(response_data)
            results_list = response_data.get('results', [])
            if results_list:
                generated_text = results_list[0].get('generated_text', '')
            else:
                generated_text = "No generated text found"
            results.append({"model": modelType, "generated_text": generated_text})

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
