import vonage
import os
from dotenv import load_dotenv

def sendMesage():
    load_dotenv()

    client = vonage.Client(key=os.getenv('VONAGE_KEY'), secret=os.getenv('VONAGE_SECRET'))
    sms = vonage.Sms(client)

    responseData = sms.send_message(
        {
            "from": "13049150279",
            "to": os.getenv('PHONE_NUMBER'),
            "text": "You are using your phone while driving",
        }
    )

    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
