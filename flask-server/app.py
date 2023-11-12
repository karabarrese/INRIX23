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
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6IjZpeWIwZGYxdGoiLCJ0b2tlbiI6eyJpdiI6ImVkZWJlYTkyZDljM2FlMzA3YTczMjRmOWU4NDU1MDMzIiwiY29udGVudCI6IjQ3ODg4Y2Q4MTgwOTlmOGJhNTM1ZDhlMmQxZjc2MzFhZDQ3NGZhN2M0OWNlZmEzZjFhYzI0MzAzZTUwNzlkNTU3ZTJmMTVlYzA5MDcxNWVhNmFlMmVhMWE5Yzg2M2JmYjU5MTBkMzBhNzgzNzQ5Y2ZjMzEzNTBmY2YwNzY4ZjA3YTk0OGFjZjFiNjRjNzAwYmYyOGY2MDU4YTFhNWJiY2E5ZTZjY2RlMzY2ZmQxY2Q3N2U0MzYyOGI1Yjg1NmMyYTVkNGYzNmY1ZmZhNjA1Zjk0NWU0MDRkYzI2ZjNmOTc5ZGI4ZGQzODUyOTYwZWNkOGIyYTAzNjM0MzQ2NWZmZDE3NjZiYzk3ZDhlZDgxMGFiMDMzOTk5MjAzYTc3OGM4Mjc2NmY5NTRlMDFhY2YxNmU5ZGNhZGZmZWUxYzZlNjFmNGFmMmNiYmQ1OTgwZTM5NGIyNTBkYjU1YmZjYTIxNDY0OTM1NWQ2NDY5MTI1MmM2ZWFlYzMzY2ZjODE1ZjA3ZTUyNzIyOGQyMDY3MWNlMzlkNWY4YzE5M2Q3MDQzM2Y3ZmVhZGRmZTIyYTI0NjMyNjIzYzM4MzMzNTQxYjk1ZTNiZmQwYTk1OWM5OWM1Mjg5NjAyYmY3NGUzZWMzYzE2YzU5M2EyODc2NmJkMDhmMzI0NDY3ZDI4MTkxOTQ4ZjlhNjIyMDI1MWNlZjg4MTFlNGQwYzEzZDdlYzZlZmJlYzc0Y2MxZDY5NzczODBhNGMyNWRjZTE4YmI0ZmM2NGExMzcxMGQxYzZjYzNhNzhjMmE2NGZmZGEzY2FjNzVmMjhjMmE3Y2NhNDBmN2VkOGYyNjRmYWJiZjA2YjUxMTFlNWMwYjY3YTlmMGRlMjE2MGUxZDRjMTdhIn0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiJlZGViZWE5MmQ5YzNhZTMwN2E3MzI0ZjllODQ1NTAzMyIsImNvbnRlbnQiOiIwZmIzODJjNjA5MTg5N2I0OWYxYWUwZjFmZWNiNmYxOGRmNTBjMDRkNWFlZjg1NWQyOWU0NTg3MDk4NWVhMjY5N2QyNjBhODI3MjM1MGRlNjMwZTllYjI0In0sImp0aSI6IjU2MjI0MzYxLTgyMWEtNDU5Yy04MzZiLTgyY2EwOWFkZmE4NSIsImlhdCI6MTY5OTgwMTMyMCwiZXhwIjoxNjk5ODA0OTIwfQ.JxubXRojuimiANV1QR4B3_qyHT9yxYcYWHGP5M0xYB',
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
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6IjZpeWIwZGYxdGoiLCJ0b2tlbiI6eyJpdiI6ImVkZWJlYTkyZDljM2FlMzA3YTczMjRmOWU4NDU1MDMzIiwiY29udGVudCI6IjQ3ODg4Y2Q4MTgwOTlmOGJhNTM1ZDhlMmQxZjc2MzFhZDQ3NGZhN2M0OWNlZmEzZjFhYzI0MzAzZTUwNzlkNTU3ZTJmMTVlYzA5MDcxNWVhNmFlMmVhMWE5Yzg2M2JmYjU5MTBkMzBhNzgzNzQ5Y2ZjMzEzNTBmY2YwNzY4ZjA3YTk0OGFjZjFiNjRjNzAwYmYyOGY2MDU4YTFhNWJiY2E5ZTZjY2RlMzY2ZmQxY2Q3N2U0MzYyOGI1Yjg1NmMyYTVkNGYzNmY1ZmZhNjA1Zjk0NWU0MDRkYzI2ZjNmOTc5ZGI4ZGQzODUyOTYwZWNkOGIyYTAzNjM0MzQ2NWZmZDE3NjZiYzk3ZDhlZDgxMGFiMDMzOTk5MjAzYTc3OGM4Mjc2NmY5NTRlMDFhY2YxNmU5ZGNhZGZmZWUxYzZlNjFmNGFmMmNiYmQ1OTgwZTM5NGIyNTBkYjU1YmZjYTIxNDY0OTM1NWQ2NDY5MTI1MmM2ZWFlYzMzY2ZjODE1ZjA3ZTUyNzIyOGQyMDY3MWNlMzlkNWY4YzE5M2Q3MDQzM2Y3ZmVhZGRmZTIyYTI0NjMyNjIzYzM4MzMzNTQxYjk1ZTNiZmQwYTk1OWM5OWM1Mjg5NjAyYmY3NGUzZWMzYzE2YzU5M2EyODc2NmJkMDhmMzI0NDY3ZDI4MTkxOTQ4ZjlhNjIyMDI1MWNlZjg4MTFlNGQwYzEzZDdlYzZlZmJlYzc0Y2MxZDY5NzczODBhNGMyNWRjZTE4YmI0ZmM2NGExMzcxMGQxYzZjYzNhNzhjMmE2NGZmZGEzY2FjNzVmMjhjMmE3Y2NhNDBmN2VkOGYyNjRmYWJiZjA2YjUxMTFlNWMwYjY3YTlmMGRlMjE2MGUxZDRjMTdhIn0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiJlZGViZWE5MmQ5YzNhZTMwN2E3MzI0ZjllODQ1NTAzMyIsImNvbnRlbnQiOiIwZmIzODJjNjA5MTg5N2I0OWYxYWUwZjFmZWNiNmYxOGRmNTBjMDRkNWFlZjg1NWQyOWU0NTg3MDk4NWVhMjY5N2QyNjBhODI3MjM1MGRlNjMwZTllYjI0In0sImp0aSI6IjU2MjI0MzYxLTgyMWEtNDU5Yy04MzZiLTgyY2EwOWFkZmE4NSIsImlhdCI6MTY5OTgwMTMyMCwiZXhwIjoxNjk5ODA0OTIwfQ.JxubXRojuimiANV1QR4B3_qyHT9yxYcYWHGP5M0xYB',
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
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6IjZpeWIwZGYxdGoiLCJ0b2tlbiI6eyJpdiI6ImVkZWJlYTkyZDljM2FlMzA3YTczMjRmOWU4NDU1MDMzIiwiY29udGVudCI6IjQ3ODg4Y2Q4MTgwOTlmOGJhNTM1ZDhlMmQxZjc2MzFhZDQ3NGZhN2M0OWNlZmEzZjFhYzI0MzAzZTUwNzlkNTU3ZTJmMTVlYzA5MDcxNWVhNmFlMmVhMWE5Yzg2M2JmYjU5MTBkMzBhNzgzNzQ5Y2ZjMzEzNTBmY2YwNzY4ZjA3YTk0OGFjZjFiNjRjNzAwYmYyOGY2MDU4YTFhNWJiY2E5ZTZjY2RlMzY2ZmQxY2Q3N2U0MzYyOGI1Yjg1NmMyYTVkNGYzNmY1ZmZhNjA1Zjk0NWU0MDRkYzI2ZjNmOTc5ZGI4ZGQzODUyOTYwZWNkOGIyYTAzNjM0MzQ2NWZmZDE3NjZiYzk3ZDhlZDgxMGFiMDMzOTk5MjAzYTc3OGM4Mjc2NmY5NTRlMDFhY2YxNmU5ZGNhZGZmZWUxYzZlNjFmNGFmMmNiYmQ1OTgwZTM5NGIyNTBkYjU1YmZjYTIxNDY0OTM1NWQ2NDY5MTI1MmM2ZWFlYzMzY2ZjODE1ZjA3ZTUyNzIyOGQyMDY3MWNlMzlkNWY4YzE5M2Q3MDQzM2Y3ZmVhZGRmZTIyYTI0NjMyNjIzYzM4MzMzNTQxYjk1ZTNiZmQwYTk1OWM5OWM1Mjg5NjAyYmY3NGUzZWMzYzE2YzU5M2EyODc2NmJkMDhmMzI0NDY3ZDI4MTkxOTQ4ZjlhNjIyMDI1MWNlZjg4MTFlNGQwYzEzZDdlYzZlZmJlYzc0Y2MxZDY5NzczODBhNGMyNWRjZTE4YmI0ZmM2NGExMzcxMGQxYzZjYzNhNzhjMmE2NGZmZGEzY2FjNzVmMjhjMmE3Y2NhNDBmN2VkOGYyNjRmYWJiZjA2YjUxMTFlNWMwYjY3YTlmMGRlMjE2MGUxZDRjMTdhIn0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiJlZGViZWE5MmQ5YzNhZTMwN2E3MzI0ZjllODQ1NTAzMyIsImNvbnRlbnQiOiIwZmIzODJjNjA5MTg5N2I0OWYxYWUwZjFmZWNiNmYxOGRmNTBjMDRkNWFlZjg1NWQyOWU0NTg3MDk4NWVhMjY5N2QyNjBhODI3MjM1MGRlNjMwZTllYjI0In0sImp0aSI6IjU2MjI0MzYxLTgyMWEtNDU5Yy04MzZiLTgyY2EwOWFkZmE4NSIsImlhdCI6MTY5OTgwMTMyMCwiZXhwIjoxNjk5ODA0OTIwfQ.JxubXRojuimiANV1QR4B3_qyHT9yxYcYWHGP5M0xYB',
    'Cookie': 'lang=en-US'
  }
  response = requests.request("GET", url, headers=headers, data=payload)
  waypoints = json.loads(response.text)["result"]["trip"]["routes"]
  return waypoints

