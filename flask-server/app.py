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
  radius = "100"
  url = f"https://api.iq.inrix.com/v1/incidents?point={point}&radius={radius}&incidentoutputfields=All&incidenttype=Incidents,Construction&locale=en"

  payload = {}
  headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6IjZpeWIwZGYxdGoiLCJ0b2tlbiI6eyJpdiI6Ijg0OWZmMmM2Nzg0YzcxN2RkN2Y3Mzc0ZWQ3ZjViNTE1IiwiY29udGVudCI6ImM0ZTVkMzJkNGM1NTJkZTFmZTY2ZGQyZWY0NDcwODNlYTE4ODA3MWU4YWQ4YjNkOTdmZDQ3OGNlYzk5MDQ1YTMyYTE2NGQ1MGM5MWI4ODdhYjU0YTBhYTE5YTFkNDY4ZTY0ODE0M2QwMmM3ZWVmZDE5MWQ1N2MyNTIxYzlhMTg4ZmNjYjZjODc3NGFkNmJkMzY0OWE4N2M5ZDYzZDEzNThkY2EyMmUzNDVlNGY5YmVmMGNiNDU4YzczZmQ0MWZlM2ZlNjY0ZGU4N2ZkZGJlZWM4MGJiZWU2ZGQxY2IyNzQ5NjgyN2IyYjQzYWIyOGNhNTcyNzFhNzUxZTcxMDBhMDkwNjJlMTQ2ODQ3YzljMjkyY2Q1OGVjMTIwY2Q3YmQwMjhlODgwMmRmOWE5ZDhhNjVhNjE3ZmE3ODkyMjlkNjQ3ZTI4MTRiODRjZDQzNjY1MzA0NDcwOGRiNjlmYmZiMzUxNDQ3MjQyYTU1YmUxY2JkZjEwN2ZhY2MxZDcyY2JiNGRlM2U1MTA3MGIzMmY5MzgyYzYzMDM4ODAzOGJhMDVmNDlhZjkwYzdlZDIxMWJlNzlhZjI5ZmViNjk3N2RhMzdlZDlhODIzMTMxMDMxNDY1OGVmYzM5MjdkYTBiMGE1ZWI0NzllNjkzZjllYWZkYjYxYTdhOTlhYzE3M2M3Mjg0MTc0ZTVhZDdhZDJlZmFjM2QyNDI2ZTM5MzEzMWVlYjg1MWMwYmY5YjA0ZTIxZTJiNTY4OTU3MWFlZDE3MGJjODYyYTkxY2E2YmJiZWVjNjJhOTVkMzkxZWFmNGYxYTEyZDZjN2U2ODEwOWQyYzRjNGY3ODdmNjhmN2M5ZTFmZTdhNGEyZmM5OGY1NWEzOTBhYWZlNmViIn0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiI4NDlmZjJjNjc4NGM3MTdkZDdmNzM3NGVkN2Y1YjUxNSIsImNvbnRlbnQiOiJkOGE5ZGUwNjFmNjEwY2ViYzkyNWZhMDNkMzRiMjkzZjljYWQzOTI1YTFkODgyYWQyNWNkN2M4YmNhYWE3ZGJmNDQxMTU0MDBhNDBmOTIwMWU1NGExNzlmIn0sImp0aSI6IjBkZDI2MmQwLWExN2EtNDdhYy1iN2EyLWJkZjI3ZDVmMTIzNiIsImlhdCI6MTY5OTgwNjgxOCwiZXhwIjoxNjk5ODEwNDE3fQ.fqlREmK6VHqdYNbFRjRMwHWCZsf0QtdlkTd9qiFw334',
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
    newJson = [i["geometry"]["coordinates"],i["descriptions"][0]["desc"]]
    incidents_json["incidents"].append(newJson)
  return incidents_json

if __name__ == "main":
  app.run(debug=True, host="0.0.0.0", port=5001)

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
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6IjZpeWIwZGYxdGoiLCJ0b2tlbiI6eyJpdiI6Ijg0OWZmMmM2Nzg0YzcxN2RkN2Y3Mzc0ZWQ3ZjViNTE1IiwiY29udGVudCI6ImM0ZTVkMzJkNGM1NTJkZTFmZTY2ZGQyZWY0NDcwODNlYTE4ODA3MWU4YWQ4YjNkOTdmZDQ3OGNlYzk5MDQ1YTMyYTE2NGQ1MGM5MWI4ODdhYjU0YTBhYTE5YTFkNDY4ZTY0ODE0M2QwMmM3ZWVmZDE5MWQ1N2MyNTIxYzlhMTg4ZmNjYjZjODc3NGFkNmJkMzY0OWE4N2M5ZDYzZDEzNThkY2EyMmUzNDVlNGY5YmVmMGNiNDU4YzczZmQ0MWZlM2ZlNjY0ZGU4N2ZkZGJlZWM4MGJiZWU2ZGQxY2IyNzQ5NjgyN2IyYjQzYWIyOGNhNTcyNzFhNzUxZTcxMDBhMDkwNjJlMTQ2ODQ3YzljMjkyY2Q1OGVjMTIwY2Q3YmQwMjhlODgwMmRmOWE5ZDhhNjVhNjE3ZmE3ODkyMjlkNjQ3ZTI4MTRiODRjZDQzNjY1MzA0NDcwOGRiNjlmYmZiMzUxNDQ3MjQyYTU1YmUxY2JkZjEwN2ZhY2MxZDcyY2JiNGRlM2U1MTA3MGIzMmY5MzgyYzYzMDM4ODAzOGJhMDVmNDlhZjkwYzdlZDIxMWJlNzlhZjI5ZmViNjk3N2RhMzdlZDlhODIzMTMxMDMxNDY1OGVmYzM5MjdkYTBiMGE1ZWI0NzllNjkzZjllYWZkYjYxYTdhOTlhYzE3M2M3Mjg0MTc0ZTVhZDdhZDJlZmFjM2QyNDI2ZTM5MzEzMWVlYjg1MWMwYmY5YjA0ZTIxZTJiNTY4OTU3MWFlZDE3MGJjODYyYTkxY2E2YmJiZWVjNjJhOTVkMzkxZWFmNGYxYTEyZDZjN2U2ODEwOWQyYzRjNGY3ODdmNjhmN2M5ZTFmZTdhNGEyZmM5OGY1NWEzOTBhYWZlNmViIn0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiI4NDlmZjJjNjc4NGM3MTdkZDdmNzM3NGVkN2Y1YjUxNSIsImNvbnRlbnQiOiJkOGE5ZGUwNjFmNjEwY2ViYzkyNWZhMDNkMzRiMjkzZjljYWQzOTI1YTFkODgyYWQyNWNkN2M4YmNhYWE3ZGJmNDQxMTU0MDBhNDBmOTIwMWU1NGExNzlmIn0sImp0aSI6IjBkZDI2MmQwLWExN2EtNDdhYy1iN2EyLWJkZjI3ZDVmMTIzNiIsImlhdCI6MTY5OTgwNjgxOCwiZXhwIjoxNjk5ODEwNDE3fQ.fqlREmK6VHqdYNbFRjRMwHWCZsf0QtdlkTd9qiFw334',
    'Cookie': 'lang=en-US'
  }

  # get all incidents from inrix api
  response = requests.request("GET", url, headers=headers, data=payload)
  currentSpeed = json.loads(response.text)["result"]["segmentspeeds"][0]["segments"][0]["speed"]
  return {"currentSegmentSpeed": currentSpeed}

@app.route('/getRoute', methods=['GET'])
def getRoute():
  url = 'https://api.iq.inrix.com/findRoute?format=json&wp_1=37.770581%2C-122.442550&wp_2=37.765297%2C-122.442527&routeOutputFields=P'
  payload = {}
  headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6IjZpeWIwZGYxdGoiLCJ0b2tlbiI6eyJpdiI6Ijg0OWZmMmM2Nzg0YzcxN2RkN2Y3Mzc0ZWQ3ZjViNTE1IiwiY29udGVudCI6ImM0ZTVkMzJkNGM1NTJkZTFmZTY2ZGQyZWY0NDcwODNlYTE4ODA3MWU4YWQ4YjNkOTdmZDQ3OGNlYzk5MDQ1YTMyYTE2NGQ1MGM5MWI4ODdhYjU0YTBhYTE5YTFkNDY4ZTY0ODE0M2QwMmM3ZWVmZDE5MWQ1N2MyNTIxYzlhMTg4ZmNjYjZjODc3NGFkNmJkMzY0OWE4N2M5ZDYzZDEzNThkY2EyMmUzNDVlNGY5YmVmMGNiNDU4YzczZmQ0MWZlM2ZlNjY0ZGU4N2ZkZGJlZWM4MGJiZWU2ZGQxY2IyNzQ5NjgyN2IyYjQzYWIyOGNhNTcyNzFhNzUxZTcxMDBhMDkwNjJlMTQ2ODQ3YzljMjkyY2Q1OGVjMTIwY2Q3YmQwMjhlODgwMmRmOWE5ZDhhNjVhNjE3ZmE3ODkyMjlkNjQ3ZTI4MTRiODRjZDQzNjY1MzA0NDcwOGRiNjlmYmZiMzUxNDQ3MjQyYTU1YmUxY2JkZjEwN2ZhY2MxZDcyY2JiNGRlM2U1MTA3MGIzMmY5MzgyYzYzMDM4ODAzOGJhMDVmNDlhZjkwYzdlZDIxMWJlNzlhZjI5ZmViNjk3N2RhMzdlZDlhODIzMTMxMDMxNDY1OGVmYzM5MjdkYTBiMGE1ZWI0NzllNjkzZjllYWZkYjYxYTdhOTlhYzE3M2M3Mjg0MTc0ZTVhZDdhZDJlZmFjM2QyNDI2ZTM5MzEzMWVlYjg1MWMwYmY5YjA0ZTIxZTJiNTY4OTU3MWFlZDE3MGJjODYyYTkxY2E2YmJiZWVjNjJhOTVkMzkxZWFmNGYxYTEyZDZjN2U2ODEwOWQyYzRjNGY3ODdmNjhmN2M5ZTFmZTdhNGEyZmM5OGY1NWEzOTBhYWZlNmViIn0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiI4NDlmZjJjNjc4NGM3MTdkZDdmNzM3NGVkN2Y1YjUxNSIsImNvbnRlbnQiOiJkOGE5ZGUwNjFmNjEwY2ViYzkyNWZhMDNkMzRiMjkzZjljYWQzOTI1YTFkODgyYWQyNWNkN2M4YmNhYWE3ZGJmNDQxMTU0MDBhNDBmOTIwMWU1NGExNzlmIn0sImp0aSI6IjBkZDI2MmQwLWExN2EtNDdhYy1iN2EyLWJkZjI3ZDVmMTIzNiIsImlhdCI6MTY5OTgwNjgxOCwiZXhwIjoxNjk5ODEwNDE3fQ.fqlREmK6VHqdYNbFRjRMwHWCZsf0QtdlkTd9qiFw334',
    'Cookie': 'lang=en-US'
  }
  response = requests.request("GET", url, headers=headers, data=payload)
  waypoints = json.loads(response.text)["result"]["trip"]["routes"]
  return waypoints

