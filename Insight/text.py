client = vonage.Client(key="8788875c", secret="9vaJoRcwLNMugM3R")
sms = vonage.Sms(client)

responseData = sms.send_message(
    {
        "from": "18503916402",
        "to": "14083480516",
        "text": "Your Child is escaping",
    }
)

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
