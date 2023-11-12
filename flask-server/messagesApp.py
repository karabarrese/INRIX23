import vonage

client = vonage.Client(key="cbfa148d", secret="b9LoLR0J5rpQp42C")
sms = vonage.Sms(client)

responseData = sms.send_message(
    {
        "from": "13049150279",
        "to": "14089669920",
        "text": "You are using your phone while driving",
    }
)

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")

responseData = sms.send_message(
    {
        "from": "13049150279",
        "to": "14089669920",
        "text": "A text message sent using the Nexmo SMS API",
    }
)

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
