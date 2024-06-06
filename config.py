# config.py


# Replace with your IBM Cloud API key
CLOUD_API_KEY = 'jQ9wd6iBHEUYhdVJma6iFewH0eYtauyazhsKGQWjIdu2'

# In most cases, the URL for authentication should be this value.
# If you get an authentication error, check the URL in IBM Cloud
AUTH_URL = 'https://iam.cloud.ibm.com/identity/token'

# Make sure to provide public, text URL (not private and not streaming)
# Prompt URL for retrieving model IDs
PROMPT_URL = 'https://us-south.ml.cloud.ibm.com/ml/v1/foundation_model_specs?version=2023-05-02&pattern=modelid_*'

# URL for generating text
GENERATE_URL = 'https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29'

# IBM Cloud Project ID
PROJECT_ID = "c6e59745-c0ca-44a2-841b-58c857227119"
