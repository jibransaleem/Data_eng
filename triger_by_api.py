
import requests

id = 12

base_url = "http://127.0.0.1:4200/api"
DEPLOYMENT_ID = "889ad6e1-82c7-42f3-9a91-4be354c7d6d5"

payload = {
    "parameters": {
        "source": id
    }
}

response = requests.post(
    f"{base_url}/deployments/{DEPLOYMENT_ID}/create_flow_run",
    json=payload
)

if response.status_code == 201:
    print("Flow run created successfully!")
    print(response.json())
else:
    print("Failed:", response.status_code)
    print(response.text)
