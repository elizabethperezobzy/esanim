import requests
from requests.auth import HTTPBasicAuth

# Set the Jira API URL
url = 'https://your-jira-url/rest/api/2/endpoint'

# Set the authentication credentials
username = 'your_username'
api_token = 'your_api_token'

# Encode the credentials in base64
credentials = f'{username}:{api_token}'
base64_credentials = base64.b64encode(credentials.encode()).decode()

# Set the headers with the Authorization header
headers = {
    'Authorization': f'Basic {base64_credentials}',
    'Content-Type': 'application/json'
}

# Make the request
response = requests.get(url, headers=headers)

# Process the response
# ...
