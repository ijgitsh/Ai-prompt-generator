# AI Prompt Generator

This repository contains an application that generates prompts using AI. The application consists of a frontend HTML page and a backend Flask API.

## Setup and Run the Application

### Prerequisites

- Python 3.7 or later 
- Flask
- Flask-CORS
- Requests

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/AI-Prompt-Generator.git
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

1. Replace the placeholder values in `app.py` with your actual access token and URLs:
    ```python
    ACCESS_TOKEN = "your_access_token"
    PROMPT_URL = "https://api.example.com/prompt"
    GENERATE_URL = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"
    ```

### Running the Application

1. Start the Flask server:
    ```bash
    python app.py
    ```

2. Open `index.html` in a web browser to use the application.

### Directory Structure

    AI-Prompt-Generator/
    ├── app.py
    ├── index.html
    ├── README.md
    ├── requirements.txt
    └── venv/


### Contributing

Feel free to submit issues and pull requests if you have any suggestions or improvements.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
