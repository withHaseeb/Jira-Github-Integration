# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask, request

app = Flask(__name__)

# Define a route that handles POST requests
@app.route('/createJira', methods=['POST'])
def createJira():
    # Parse the GitHub webhook payload
    github_payload = request.get_json()

    # Check if the payload contains a comment and the comment body is "create_jira"
    if 'comment' in github_payload and 'create_jira' in github_payload['comment']['body'].lower():
        # Jira API request code (unchanged from your original code)
        url = "https://withhaseeb.atlassian.net/rest/api/3/issue"
        apitoken = "<your token>"
        auth = HTTPBasicAuth("with.haseeb@gmail.com", apitoken)

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        payload = json.dumps({
            "fields": {
                "description": {
                    "content": [
                        {
                            "content": [
                                {
                                    "text": "Order entry fails when selecting supplier.",
                                    "type": "text"
                                }
                            ],
                            "type": "paragraph"
                        }
                    ],
                    "type": "doc",
                    "version": 1
                },
                "project": {
                    "key": "<your project key>"
                },
                "issuetype": {
                    "id": "10006"
                },
                "summary": "Main order flow broken",
            },
            "update": {}
        })

        response = requests.request(
            "POST",
            url,
            data=payload,
            headers=headers,
            auth=auth
        )

        return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    else:
        # Return a message indicating that no Jira ticket was created
        return "No Jira ticket created. Comment does not contain 'create_jira'."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
