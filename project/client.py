import requests

# Step 1: Client requests a token from OAuth

# Parameters for token request
client_id = 'your_client_id'
client_secret = 'your_client_secret'
redirect_uri = 'http://localhost:8000/callback'
authorization_endpoint = 'http://localhost:8000/authorize'
token_endpoint = 'http://localhost:8000/token'

# Redirect the user to the authorization endpoint
authorization_url = authorization_endpoint + '?client_id=' + client_id
print("Please visit the following URL and provide consent:")
print(authorization_url)

# Receive the authorization code from the callback URL
authorization_code = input("Enter the authorization code: ")

# Exchange the authorization code for an access token
token_params = {
    'code': authorization_code,
    'client_id': client_id,
    'client_secret': client_secret,
    'redirect_uri': redirect_uri
}
response = requests.post(token_endpoint, data=token_params)

if response.status_code == 200:
    token_data = response.json()
    access_token = token_data.get('access_token')
    token_type = token_data.get('token_type')
    expires_in = token_data.get('expires_in')
    if 'access_token' in token_data:
        # Step 4: OAuth sends access token to the client
        access_token = token_data['access_token']
        print("Access token:", access_token)

        # Step 5: Client sends token and requests resources from the resource server
        resource_server_url = 'http://localhost:5000/resource'
        headers = {'Authorization': 'Bearer ' + access_token}
        resource_response = requests.get(resource_server_url, headers=headers)

        if resource_response.status_code == 200:
            # Step 7: The resource server sends resources to the client
            print("Resources:")
            print(resource_response.json())
        else:
            print("Error accessing resources:", resource_response.status_code)
    else:
        print("Error: No access token found in token response")
else:
    print("Error requesting access token:", response.status_code)


