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
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6IjZpeWIwZGYxdGoiLCJ0b2tlbiI6eyJpdiI6Ijc2ZmYzNTlhNTE3NWI5NjM5ZmQyZWQ1NTM0YTNhOTFkIiwiY29udGVudCI6IjRkYTA1YmFkZGMxZTI2ZTk0ZTlhNjdmZjhkZTBkYzI2YjE3YTIyMzZhMThhYmViZWFlZmIwOGQyZTQwZWM2ZDgzZGUwNGFlYTcxZDA2MWUwM2FjMDJmNjE2NjA1YWEwYWFmNDhkMmEzYWJkOTFjZmI0MWVlZjU4ZDRmNDRlMzA2MDkwNGEyOTY5MmJiOTJjMDAwZTZjNjQxNmU0ZjRmZWMwMTU5NThkMDUyMWFiNzhmYjBiOWM3YjA1MTJkNzljNGIxNjljNzYzMDQ2MzliNzYxOTVhNmYwMGM4ZmI2ZTYyYzM3NjEzYzg5OWM2OGJiNGE3MTE5MTEyY2FkMTY1NjQxN2EyZDcyODg0YjBkMjU1ODdjOWFiNjM0MGYwM2ZhY2VmZDc4NTY4MTBhNjVjYTQ5NWEwMWZkYzRmMzZiYzVmNGYzYThmNmU2ZDZhYzFkMTI5MTdmMGVhNTMwNjBjYmY2MWFmYTYxODVmNWVhZTgzZDMyNDUwNTk4ZjE1NTgxZThlNzQxZDJjZjIyNmJiY2I0MjNhZjAxZTFjMTdhMWNjYmUxNTVlYzgzYWVlMTc0N2MzZmE4OGI4MGJmNjgyNmNmM2ExZDYwOWI4ZDVkNWFkOGMyNjM4N2UzNWU4ZWM4OTgwM2ZmNTU5YzI4MDY3MDUyOWEzYjIxMTY1N2YxZDE3ZTlkNzQ3NDk3ZjZjODMxYTk1NjJlZjQwMTZiMjkyYmRlMWQxNmEwY2Y1N2EyNmVkYzE0YzM4MzY0ZDc0ZTIwMmQyODIwZjczNTdmNTgxMzI3ZDRmNmQ0ZWVhZGNlOGRhM2RjMWE0M2JiNzk4ZjQzNjBmZWY1OWI5ODNiYjZlNWNmYWQxMjFiM2VhNGEyYmMxMGIwYmFiIn0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiI3NmZmMzU5YTUxNzViOTYzOWZkMmVkNTUzNGEzYTkxZCIsImNvbnRlbnQiOiI2ZGJjNjhhZjg4MWEwN2Q3NTM5OTU0ZjE4OWQyZmI2M2NlNTIwZTAzZGRkMDg4ZjJhMmNlMmJhYmUyMjNkOWUyMTNmNTU3ZTUxN2ZlNzBmZjM1YzgwMDVmIn0sImp0aSI6ImZjZTU3MTliLTMwYTctNGJjYi1iOTVkLTJlZDRjMzVlNmY4YiIsImlhdCI6MTY5OTc5MDI4NCwiZXhwIjoxNjk5NzkzODg0fQ.LdOHJrXQ0zbLYs3EkOrW7hynTjcRE85Zxexoy8R-dV4',
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
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6IjZpeWIwZGYxdGoiLCJ0b2tlbiI6eyJpdiI6Ijc2ZmYzNTlhNTE3NWI5NjM5ZmQyZWQ1NTM0YTNhOTFkIiwiY29udGVudCI6IjRkYTA1YmFkZGMxZTI2ZTk0ZTlhNjdmZjhkZTBkYzI2YjE3YTIyMzZhMThhYmViZWFlZmIwOGQyZTQwZWM2ZDgzZGUwNGFlYTcxZDA2MWUwM2FjMDJmNjE2NjA1YWEwYWFmNDhkMmEzYWJkOTFjZmI0MWVlZjU4ZDRmNDRlMzA2MDkwNGEyOTY5MmJiOTJjMDAwZTZjNjQxNmU0ZjRmZWMwMTU5NThkMDUyMWFiNzhmYjBiOWM3YjA1MTJkNzljNGIxNjljNzYzMDQ2MzliNzYxOTVhNmYwMGM4ZmI2ZTYyYzM3NjEzYzg5OWM2OGJiNGE3MTE5MTEyY2FkMTY1NjQxN2EyZDcyODg0YjBkMjU1ODdjOWFiNjM0MGYwM2ZhY2VmZDc4NTY4MTBhNjVjYTQ5NWEwMWZkYzRmMzZiYzVmNGYzYThmNmU2ZDZhYzFkMTI5MTdmMGVhNTMwNjBjYmY2MWFmYTYxODVmNWVhZTgzZDMyNDUwNTk4ZjE1NTgxZThlNzQxZDJjZjIyNmJiY2I0MjNhZjAxZTFjMTdhMWNjYmUxNTVlYzgzYWVlMTc0N2MzZmE4OGI4MGJmNjgyNmNmM2ExZDYwOWI4ZDVkNWFkOGMyNjM4N2UzNWU4ZWM4OTgwM2ZmNTU5YzI4MDY3MDUyOWEzYjIxMTY1N2YxZDE3ZTlkNzQ3NDk3ZjZjODMxYTk1NjJlZjQwMTZiMjkyYmRlMWQxNmEwY2Y1N2EyNmVkYzE0YzM4MzY0ZDc0ZTIwMmQyODIwZjczNTdmNTgxMzI3ZDRmNmQ0ZWVhZGNlOGRhM2RjMWE0M2JiNzk4ZjQzNjBmZWY1OWI5ODNiYjZlNWNmYWQxMjFiM2VhNGEyYmMxMGIwYmFiIn0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiI3NmZmMzU5YTUxNzViOTYzOWZkMmVkNTUzNGEzYTkxZCIsImNvbnRlbnQiOiI2ZGJjNjhhZjg4MWEwN2Q3NTM5OTU0ZjE4OWQyZmI2M2NlNTIwZTAzZGRkMDg4ZjJhMmNlMmJhYmUyMjNkOWUyMTNmNTU3ZTUxN2ZlNzBmZjM1YzgwMDVmIn0sImp0aSI6ImZjZTU3MTliLTMwYTctNGJjYi1iOTVkLTJlZDRjMzVlNmY4YiIsImlhdCI6MTY5OTc5MDI4NCwiZXhwIjoxNjk5NzkzODg0fQ.LdOHJrXQ0zbLYs3EkOrW7hynTjcRE85Zxexoy8R-dV4',
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
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6IjZpeWIwZGYxdGoiLCJ0b2tlbiI6eyJpdiI6Ijc2ZmYzNTlhNTE3NWI5NjM5ZmQyZWQ1NTM0YTNhOTFkIiwiY29udGVudCI6IjRkYTA1YmFkZGMxZTI2ZTk0ZTlhNjdmZjhkZTBkYzI2YjE3YTIyMzZhMThhYmViZWFlZmIwOGQyZTQwZWM2ZDgzZGUwNGFlYTcxZDA2MWUwM2FjMDJmNjE2NjA1YWEwYWFmNDhkMmEzYWJkOTFjZmI0MWVlZjU4ZDRmNDRlMzA2MDkwNGEyOTY5MmJiOTJjMDAwZTZjNjQxNmU0ZjRmZWMwMTU5NThkMDUyMWFiNzhmYjBiOWM3YjA1MTJkNzljNGIxNjljNzYzMDQ2MzliNzYxOTVhNmYwMGM4ZmI2ZTYyYzM3NjEzYzg5OWM2OGJiNGE3MTE5MTEyY2FkMTY1NjQxN2EyZDcyODg0YjBkMjU1ODdjOWFiNjM0MGYwM2ZhY2VmZDc4NTY4MTBhNjVjYTQ5NWEwMWZkYzRmMzZiYzVmNGYzYThmNmU2ZDZhYzFkMTI5MTdmMGVhNTMwNjBjYmY2MWFmYTYxODVmNWVhZTgzZDMyNDUwNTk4ZjE1NTgxZThlNzQxZDJjZjIyNmJiY2I0MjNhZjAxZTFjMTdhMWNjYmUxNTVlYzgzYWVlMTc0N2MzZmE4OGI4MGJmNjgyNmNmM2ExZDYwOWI4ZDVkNWFkOGMyNjM4N2UzNWU4ZWM4OTgwM2ZmNTU5YzI4MDY3MDUyOWEzYjIxMTY1N2YxZDE3ZTlkNzQ3NDk3ZjZjODMxYTk1NjJlZjQwMTZiMjkyYmRlMWQxNmEwY2Y1N2EyNmVkYzE0YzM4MzY0ZDc0ZTIwMmQyODIwZjczNTdmNTgxMzI3ZDRmNmQ0ZWVhZGNlOGRhM2RjMWE0M2JiNzk4ZjQzNjBmZWY1OWI5ODNiYjZlNWNmYWQxMjFiM2VhNGEyYmMxMGIwYmFiIn0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiI3NmZmMzU5YTUxNzViOTYzOWZkMmVkNTUzNGEzYTkxZCIsImNvbnRlbnQiOiI2ZGJjNjhhZjg4MWEwN2Q3NTM5OTU0ZjE4OWQyZmI2M2NlNTIwZTAzZGRkMDg4ZjJhMmNlMmJhYmUyMjNkOWUyMTNmNTU3ZTUxN2ZlNzBmZjM1YzgwMDVmIn0sImp0aSI6ImZjZTU3MTliLTMwYTctNGJjYi1iOTVkLTJlZDRjMzVlNmY4YiIsImlhdCI6MTY5OTc5MDI4NCwiZXhwIjoxNjk5NzkzODg0fQ.LdOHJrXQ0zbLYs3EkOrW7hynTjcRE85Zxexoy8R-dV4',
    'Cookie': 'lang=en-US'
  }
  response = requests.request("GET", url, headers=headers, data=payload)
  waypoints = json.loads(response.text)["result"]["trip"]["routes"]
  return waypoints

