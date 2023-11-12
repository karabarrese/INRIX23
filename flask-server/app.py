import json
import requests
from flask import Flask, jsonify, request

import vonage
import os
from dotenv import load_dotenv

app = Flask(__name__)

@app.route('/incidents', methods=['GET'])
def index():
  # args = request.args
  # point = args.get("point", default="37.757386|-122.490667", type=str)

  point = "37.757386|-122.490667"
  # box = "37.757386|-122.490667,37.746138|-122.395481"
  radius = "100"
  url = f"https://api.iq.inrix.com/v1/incidents?point={point}&radius={radius}&incidentoutputfields=All&incidenttype=Incidents,Construction&locale=en"

  payload = {}
  headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6IjZpeWIwZGYxdGoiLCJ0b2tlbiI6eyJpdiI6ImJiOWE1MjFkY2YzZjE4YzRmOTAwZGEzYjNiMTZmMjc2IiwiY29udGVudCI6IjhhMzViZTFjZmExYTExNjE1ODkxNjU2MjhmZTRjZmM3NWI1NDc0MjMwYjRmNWQ5YTFkNmI4NDkxMDFmNDE1ZWUwYjYwMjE0ZTQ5MjU2MjhlNjk4MTY1OTJhYWQyNDFlOTgzZjMzYmMyNmFkM2E5MTY0YWU2NDZhYmM4YzU3MmU1MzQxZmNiODQ2NmNkZDdiODZjOTBmMTIwZTllNzg4YjNlZDkyNzZhNGUzYmMxMzU1YmRkMjEyNDBhMWU4OWQ5NGRhYmVjNjU4MmNmNmU2MTE0ZWQ4MzI4MGExNjhlMDYzMjUyZDAwZmY1YTM1NjhiNDY0ZGMxZjgzMzA4NGY1MTFkNTA0ZTBkYTdmNmE0MjBjZTE2MzNmNWU5YWQ4MjIyMjQ4MWQzNDY5YzM2Y2Y5MTRkMThiZTNjYTc4ZDYzMzA1ZjFkZDNiMjgxNDI0MjdkZWQ1M2Q2NWI2MjJhNmRiYWFlZTIxZGM1MzkyNTQyMjkxZmZjYjdjMWE1ZTcyZmVmOTIyN2Y1YzdmOTE2MjQ3NDA1ZDM5ODk1MmU2ZWYzNWMyNGMyYTJhMDJhYTcyYWMyYWQzNzZmOWZiYzQxMzZkZGJiNjQwNzk2MDBlNzA2ZTVkODdkNmNmMmMyMmMwNDNhMzRjMGZlOWZmOThmNDRkZDkwMjgwOGQ4OTEwZDI2NWNlODAxOGNjODgwM2I1ZGNkNDYwZTkwODVlN2Q1ZDNkNjJmMWM5NTgwZjU1ZWIwNTgyNmU1ZTM0NzgyODhkNzQzZWQyMjY0MDgxNTY3MzIxZWI3MzdkOGVkNjE5MzEzYzIzYzdmNDM4NDAxNDI3ZDY5M2ZmMGZhZDM4ODQ3YzVmNTFlMjcwZGRmYzQ1MTVhNjY2MTRlYjRkIn0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiJiYjlhNTIxZGNmM2YxOGM0ZjkwMGRhM2IzYjE2ZjI3NiIsImNvbnRlbnQiOiI5YTYxOGMyNmQxM2UzOTZiNDFiMjFlNDU5MWM3YjVjNzdhNzI1MTNlNzAwYjZhOWIxMjZjOTdjZTEyZGEyN2M1MGU0NDQxNGYyOTEzNWE4OTUzZGI0ZWFjIn0sImp0aSI6ImZhOGFjYmQ1LTA3OTYtNDAyZC1iZWUxLTMzYTA2OWM1YzA5MiIsImlhdCI6MTY5OTc2NjUwMCwiZXhwIjoxNjk5NzcwMTAwfQ.Fx_sniZkGPTgIHICnnugqAfVWLzE3QitdHnsgzTBAWQ',
    'Cookie': 'lang=en-US'
  }

  # get all incidents from inrix api
  response = requests.request("GET", url, headers=headers, data=payload)
  incidents = json.loads(response.text)["result"]["incidents"]

  my_dict = {"incidents": []}
  my_json = json.dumps(my_dict)
  incidents_json = json.loads(my_json)

  # filter out just coordinates and description data in array
  for i in incidents:
    # data_array.append([incidents[0]["geometry"]["coordinates"],i["descriptions"][0]["desc"]])
    newJson = [i["geometry"]["coordinates"],i["descriptions"][0]["desc"]]
    # newJson = {"location": i["geometry"]["coordinates"],"description": i["descriptions"][0]["desc"]}
    incidents_json["incidents"].append(newJson)
  return incidents_json

if __name__ == "main":
  app.run(debug=True, host="0.0.0.0", port=5001)

@app.route('/add_todo', methods=['GET'])
def add_todo():
  print("todo function running")
  return {"test": "yay!"}

@app.route('/sendMessage', methods=['POST'])
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
    return