# AI Prompt Generator

This repository contains an application that generates prompts using AI. The application consists of a frontend HTML page and a backend Flask API.
Accompanying Article : https://imanjohari.medium.com/ai-prompt-engineering-assistant-4e52d9f90f60

## Overview

Click the image below to download and watch the overview video:

[![Watch the video](https://github.com/ijgitsh/Ai-prompt-generator/blob/main/aigent.png)](https://github.com/ijgitsh/Ai-prompt-generator/blob/main/ai-prompt-gen.mp4)


## Setup and Run the Application

### Prerequisites

- Python 3.7 or later 
- Flask
- Flask-CORS
- Requests

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ijgitsh/AI-Prompt-Generator.git
    cd AI-Prompt-Generator
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install Flask Flask-CORS requests
    ```

### Configuration

1. Replace the placeholder values in `config.py` with your actual access token and URLs:
    ```python
    ACCESS_TOKEN = "your_access_token"
    CLOUD_API_KEY = "your_cloud_api_key"
    AUTH_URL = "https://iam.cloud.ibm.com/identity/token"
    PROMPT_URL = "https://us-south.ml.cloud.ibm.com/ml/v1/foundation_model_specs?version=2023-05-02&pattern=modelid_*"
    GENERATE_URL = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"
    PROJECT_ID = "your_project_id"
    ```

### Running the Application

1. Start the Flask server:
    ```bash
    python modelserver.py
    ```

2. Open `index.html` in a web browser to use the application.
3. Click on the hamburger menu on the top left
4. Select foundation models you want to use to generate your prompt
5. In the input box give a short description of what you want to do 
    ```bash
    e.g. a prompt to classify an email with time-sensitive or non-time-sensitive - my output should be json
    e.g. a prompt to extract places, dates and people 
    ```
6. ATTENTION: THE MORE MODELS YOU CHOOSE, THE LONGER YOU NEED TO WAIT - TRY COUPLE OF MODELS FIRST AND THEN EXPAND 

### Directory Structure

    AI-Prompt-Generator/
    ├── modelserver.py
    ├── index.html
    ├── README.md
    ├── requirements.txt
    ├── ai-prompt-gen.mp4
    └── aigent.png


### Contributing

Feel free to submit issues and pull requests if you have any suggestions or improvements.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
