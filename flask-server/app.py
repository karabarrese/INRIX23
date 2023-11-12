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
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6IjZpeWIwZGYxdGoiLCJ0b2tlbiI6eyJpdiI6ImVmNTc5YmVhNDg4YjNhNWJkNzJlZjllZTFlNGFlYjhkIiwiY29udGVudCI6ImZjNWQ2YjgwZDlkNGRkMzEyZWFhMmQxMDA2MTg0NTQ5MzUyZDRmNTYyODBhZmFhYmQzZjBkNjI2MjI0MDJlMTdkYjI1OGQyZTBhM2YwNWUyYTY0NDdhZGI0ZTg4ZjQ0N2M4NzcyMzU1ZjRkMjI2Yjc1YzNmZDY0OTM4YzdiMGMzZWZmYmY2NjE3NmRmMWUyM2VlZjhiYmRlYjQ4YjJkOGE0MDk3OWU5YzA0YTA4YzM5ZTIwNWVlNDc3NDJlZTc1Mjc4Yjc3MWM1MzM5MWU4YWRiOTNkNWEzYTNmMjA1YTQ4Y2Q4NzIyNzVmM2RlMDk4YjU4YmZmZjZkNGVkNDliZTM3ZmI5MjY1NjU1NWNmZDMwNTcwYjlhNjJhMTUxNGFkMTNiZmE4NjUzOGU0ZmE0MzViMTBiNjA1MWE0NTk1MTQ4MjE2MDkzZjQ1NjA5MTMzNzZlNDA1YzY2N2NkY2JmYTM2NjNlYTNkOTkyM2E4ZTlkM2IzYzA4MmE1MDExOTE1NGY5OTcxNDZhNmVmYjMyZjQ4ODBiYmI1ODA5YjY3OWVlNWVlZjRiMTcwNWExMzYzMTQzYTc2MjU2MTY4MmExZmFiNWVkYWViM2Q5NGI5OWY4OWY4YWVlNTExNjA5MzAxYjBhOTAwZWE4OTJmMDU1YzdjOTJlMmZlMmI5NzA2YmNhMzczNTU5MTc5YmJiMWEwN2NlMWY2NDllOGE0NWUwZjkwNGI1YWU2YzIxNjY5YjUxYmI0ZTRhNTJiMGU2NWMwNDlkYTdkMmU3MWQ1ODg0MTkyZGYzYmE5MTMxMGZhZTE2YmJiYzg3OTkzOWExYzc1YzlkYjNjOGYzYWFlYmU5NDE0MGU4MGQzMDVhY2YzZTdjZjA0Yzc3In0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiJlZjU3OWJlYTQ4OGIzYTViZDcyZWY5ZWUxZTRhZWI4ZCIsImNvbnRlbnQiOiJmNjYwNTJiYThkZTA5NDZkMjdhZjEwMmYzNTE1NjAxYjNhMzA1NTUxMTQyMWU2YzllN2NhZTgyMTNlN2QxZjI5ZGY1MGJlNTQ1NTNkMDhjYWY3MWY3YmU1In0sImp0aSI6IjNkZGRhNjc2LTVlY2ItNDNmYi1hNzQyLTVlNmQ1YjhiZDAzZSIsImlhdCI6MTY5OTc4MDY0NCwiZXhwIjoxNjk5Nzg0MjQ0fQ.IFtNIe7Ovz5BmdDLFpFC23IbNg60mADXaFROeFYDmCg',
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
    # newJson = [i["geometry"]["coordinates"],i["descriptions"][0]["desc"],i["schedule"]["occurrenceStartTime"], i["schedule"]["occurrenceEndTime"]]
    # newJson = {"location": i["geometry"]["coordinates"],"description": i["descriptions"][0]["desc"]}
    incidents_json["incidents"].append(newJson)
  return incidents_json

if __name__ == "main":
  app.run(debug=True, host="0.0.0.0", port=5001)

# @app.route('/add_todo', methods=['GET'])
# def add_todo():
#   print("todo function running")
#   return {"test": "yay!"}

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

@app.route('/sendSpeedMessage', methods=['POST'])
def sendSpeedMesage():
  load_dotenv()
  client = vonage.Client(key=os.getenv('VONAGE_KEY'), secret=os.getenv('VONAGE_SECRET'))
  sms = vonage.Sms(client)

  responseData = sms.send_message(
      {
          "from": "13049150279",
          "to": os.getenv('PHONE_NUMBER'),
          "text": "You are driving too fast",
      }
  )

  if responseData["messages"][0]["status"] == "0":
      print("Message sent successfully.")
  else:
      print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
  return


@app.route('/segmentSpeed', methods=['GET'])
def speedIndex():
  point = "37.757386%7C-122.490667"
  radius = "0.1"
  url = f"https://api.iq.inrix.com/v1/segments/speed?point={point}&radius={radius}"
  # url = "https://api.iq.inrix.com/v1/segments/speed?point=37.757386%7C-122.490667&radius=0.1"
  payload = {}
  headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6IjZpeWIwZGYxdGoiLCJ0b2tlbiI6eyJpdiI6ImVmNTc5YmVhNDg4YjNhNWJkNzJlZjllZTFlNGFlYjhkIiwiY29udGVudCI6ImZjNWQ2YjgwZDlkNGRkMzEyZWFhMmQxMDA2MTg0NTQ5MzUyZDRmNTYyODBhZmFhYmQzZjBkNjI2MjI0MDJlMTdkYjI1OGQyZTBhM2YwNWUyYTY0NDdhZGI0ZTg4ZjQ0N2M4NzcyMzU1ZjRkMjI2Yjc1YzNmZDY0OTM4YzdiMGMzZWZmYmY2NjE3NmRmMWUyM2VlZjhiYmRlYjQ4YjJkOGE0MDk3OWU5YzA0YTA4YzM5ZTIwNWVlNDc3NDJlZTc1Mjc4Yjc3MWM1MzM5MWU4YWRiOTNkNWEzYTNmMjA1YTQ4Y2Q4NzIyNzVmM2RlMDk4YjU4YmZmZjZkNGVkNDliZTM3ZmI5MjY1NjU1NWNmZDMwNTcwYjlhNjJhMTUxNGFkMTNiZmE4NjUzOGU0ZmE0MzViMTBiNjA1MWE0NTk1MTQ4MjE2MDkzZjQ1NjA5MTMzNzZlNDA1YzY2N2NkY2JmYTM2NjNlYTNkOTkyM2E4ZTlkM2IzYzA4MmE1MDExOTE1NGY5OTcxNDZhNmVmYjMyZjQ4ODBiYmI1ODA5YjY3OWVlNWVlZjRiMTcwNWExMzYzMTQzYTc2MjU2MTY4MmExZmFiNWVkYWViM2Q5NGI5OWY4OWY4YWVlNTExNjA5MzAxYjBhOTAwZWE4OTJmMDU1YzdjOTJlMmZlMmI5NzA2YmNhMzczNTU5MTc5YmJiMWEwN2NlMWY2NDllOGE0NWUwZjkwNGI1YWU2YzIxNjY5YjUxYmI0ZTRhNTJiMGU2NWMwNDlkYTdkMmU3MWQ1ODg0MTkyZGYzYmE5MTMxMGZhZTE2YmJiYzg3OTkzOWExYzc1YzlkYjNjOGYzYWFlYmU5NDE0MGU4MGQzMDVhY2YzZTdjZjA0Yzc3In0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiJlZjU3OWJlYTQ4OGIzYTViZDcyZWY5ZWUxZTRhZWI4ZCIsImNvbnRlbnQiOiJmNjYwNTJiYThkZTA5NDZkMjdhZjEwMmYzNTE1NjAxYjNhMzA1NTUxMTQyMWU2YzllN2NhZTgyMTNlN2QxZjI5ZGY1MGJlNTQ1NTNkMDhjYWY3MWY3YmU1In0sImp0aSI6IjNkZGRhNjc2LTVlY2ItNDNmYi1hNzQyLTVlNmQ1YjhiZDAzZSIsImlhdCI6MTY5OTc4MDY0NCwiZXhwIjoxNjk5Nzg0MjQ0fQ.IFtNIe7Ovz5BmdDLFpFC23IbNg60mADXaFROeFYDmCg',
    'Cookie': 'lang=en-US'
  }

  # get all incidents from inrix api
  response = requests.request("GET", url, headers=headers, data=payload)
  currentSpeed = json.loads(response.text)["result"]["segmentspeeds"][0]["segments"][0]["speed"]
  return {"currentSegmentSpeed": currentSpeed}
