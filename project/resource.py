from flask import Flask, jsonify, request

app = Flask(__name__)

# Step 6: Resource server receives a request with an access token and validates it
@app.route('/resource', methods=['GET'])
def resource():
    access_token = request.headers.get('Authorization').split(' ')[1]

    # Validate the access token
    if validate_access_token(access_token):
        # Step 7: The resource server sends resources to the client
        return jsonify({'resources': ['ali', 'amin']}), 200
    else:
        return jsonify({'error': 'Invalid token'}), 401

def validate_access_token(access_token):
    # Add your access token validation logic here
    # For demonstration purposes, let's assume the token is valid
    return True

if __name__ == '__main__':
    app.run(port=5000)

