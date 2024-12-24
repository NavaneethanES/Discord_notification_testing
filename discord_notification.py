import requests

def send_discord_notification():
    webhook_url = "https://discord.com/api/webhooks/1321212281056526347/fPC_50FEJpL2d79C3tEHeeXI1-7UeKK-DQmzWWzyojN3qQ_MlS1eRB3O2A1GI6J9jX3f"  # Replace with your webhook URL
    message = "Hello! This is an automated notification from GitHub Actions."
    
    payload = {"content": message}
    headers = {"Content-Type": "application/json"}
    
    response = requests.post(webhook_url, json=payload, headers=headers)
    if response.status_code == 204:
        print("Notification sent successfully!")
    else:
        print(f"Failed to send notification: {response.status_code} - {response.text}")

# Run the function
if __name__ == "__main__":
    send_discord_notification()