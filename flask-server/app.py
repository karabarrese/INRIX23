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
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6IjZpeWIwZGYxdGoiLCJ0b2tlbiI6eyJpdiI6ImMzYmJiMDkxNmI2MGM0ODY2Mjc3ZTEyMTlhMmZiNzcyIiwiY29udGVudCI6IjgxNGRkMzQ3M2ZkZGZkMjkzODE4NmMyMzZlOWEzY2Q1NWY5NTQzYjU3YmQ0ODRjNDk0YTAwYjBhNGEwM2RkZDI3MDVhMmI1YTc5ODkyMGE1ZDk0ZGFlYTM3MzQ5Y2E2ZDkyNzAzMzYwMGY2OTk5YTNmZmExOGVhYmQwYmY2ZDE2ODc1OWU4ODRjMzE4NmQ2MWY4ODA5ZDIyZTRmNTMyZGFiNTE5MTFlMDhiODQ1YjJhZGIyMzRhOWRlNjIzZmVmYzU4YTRjYWU1MGVmODUwYWFhYmQyNTg3M2JhYjRhZjkxYWZiNGY1NzgwYzU3MTQ1MDQ4ZmYyNTM2NDNiZmMxMzM2MzcyOWRiMTlhYzkwZTc2NWNjNzc3OWJkMDJkYzdhNzViMjFkNmE2NTk0N2VmMzBjNTFjNDk5MmE2MzI3ZjY1MTcyODk3NWJhMDlmZjcwODg2MThhMDc2NGRiNTkzM2RmMTAyYTczOThmNDIwMDk4NWI5NTI5NjQ5ODg3YjdiZGI2ZDNjNzMxMjU2OTI1NjcxNThiNTU3MzU5Yzk1OGQ0OTA1ZDQ3M2E1YjFiNzM4NGFhMGVhMGZjNGJkNmVlNWRhMDIzZmMwNWVkM2Q4Y2RiMDkyYmQzMTE5MDZhODEyOTM5N2U3YmYzNzMwMmJmMjBlOTgyZjRjNzM0MjZiMThlNDhkODAyZjdjMTA4ODM3OTMwNDE5ZTdkZTU5OGMyNjMxYzA2YjRhN2Q3Njk0ZGJhMDM0ZTk0ZTllODNmZGY4Mjg0NjcxNGQ3MTVjOWE2NjMxNjlkN2NkYzA0ZWU3YjU3NTY0M2U0Yzc0YjAxZjQ3MjMyODRiOTdjMTA2YzFiNmI3YTdjNmVhZTA2NzcxNTVlZTUifSwic2VjdXJpdHlUb2tlbiI6eyJpdiI6ImMzYmJiMDkxNmI2MGM0ODY2Mjc3ZTEyMTlhMmZiNzcyIiwiY29udGVudCI6Ijk1NDRkZDc4MjdlZGE2MTMyZTAxNGIyMjQyODcxMGE4N2I5NzdkZjE1NzhiYmZiMjg1Yjc3MzdkNjAxY2Q1ZjM2MzYxMjIwODNiYTMzNWJhZDIxNmQ2OWQifSwianRpIjoiMzFhYTg3ZjEtMWY1Zi00ODIwLWJhZDgtMzRmNzhlMjdiOGJjIiwiaWF0IjoxNjk5Nzc0MjU3LCJleHAiOjE2OTk3Nzc4NTd9.Q1PX5x7sWJlJbzFVpjHcIySTvxoX0uh7IGtlgI18E94',
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


@app.route('/segmentSpeed', methods=['GET'])
def speedIndex():
  point = "37.757386%7C-122.490667"
  radius = "0.1"
  # url = f"https://api.iq.inrix.com/v1/segments/speed?point={point}&radius={radius}"
  url = "https://api.iq.inrix.com/v1/segments/speed?point=37.757386%7C-122.490667&radius=0.1"
  payload = {}
  headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6IjZpeWIwZGYxdGoiLCJ0b2tlbiI6eyJpdiI6ImMzYmJiMDkxNmI2MGM0ODY2Mjc3ZTEyMTlhMmZiNzcyIiwiY29udGVudCI6IjgxNGRkMzQ3M2ZkZGZkMjkzODE4NmMyMzZlOWEzY2Q1NWY5NTQzYjU3YmQ0ODRjNDk0YTAwYjBhNGEwM2RkZDI3MDVhMmI1YTc5ODkyMGE1ZDk0ZGFlYTM3MzQ5Y2E2ZDkyNzAzMzYwMGY2OTk5YTNmZmExOGVhYmQwYmY2ZDE2ODc1OWU4ODRjMzE4NmQ2MWY4ODA5ZDIyZTRmNTMyZGFiNTE5MTFlMDhiODQ1YjJhZGIyMzRhOWRlNjIzZmVmYzU4YTRjYWU1MGVmODUwYWFhYmQyNTg3M2JhYjRhZjkxYWZiNGY1NzgwYzU3MTQ1MDQ4ZmYyNTM2NDNiZmMxMzM2MzcyOWRiMTlhYzkwZTc2NWNjNzc3OWJkMDJkYzdhNzViMjFkNmE2NTk0N2VmMzBjNTFjNDk5MmE2MzI3ZjY1MTcyODk3NWJhMDlmZjcwODg2MThhMDc2NGRiNTkzM2RmMTAyYTczOThmNDIwMDk4NWI5NTI5NjQ5ODg3YjdiZGI2ZDNjNzMxMjU2OTI1NjcxNThiNTU3MzU5Yzk1OGQ0OTA1ZDQ3M2E1YjFiNzM4NGFhMGVhMGZjNGJkNmVlNWRhMDIzZmMwNWVkM2Q4Y2RiMDkyYmQzMTE5MDZhODEyOTM5N2U3YmYzNzMwMmJmMjBlOTgyZjRjNzM0MjZiMThlNDhkODAyZjdjMTA4ODM3OTMwNDE5ZTdkZTU5OGMyNjMxYzA2YjRhN2Q3Njk0ZGJhMDM0ZTk0ZTllODNmZGY4Mjg0NjcxNGQ3MTVjOWE2NjMxNjlkN2NkYzA0ZWU3YjU3NTY0M2U0Yzc0YjAxZjQ3MjMyODRiOTdjMTA2YzFiNmI3YTdjNmVhZTA2NzcxNTVlZTUifSwic2VjdXJpdHlUb2tlbiI6eyJpdiI6ImMzYmJiMDkxNmI2MGM0ODY2Mjc3ZTEyMTlhMmZiNzcyIiwiY29udGVudCI6Ijk1NDRkZDc4MjdlZGE2MTMyZTAxNGIyMjQyODcxMGE4N2I5NzdkZjE1NzhiYmZiMjg1Yjc3MzdkNjAxY2Q1ZjM2MzYxMjIwODNiYTMzNWJhZDIxNmQ2OWQifSwianRpIjoiMzFhYTg3ZjEtMWY1Zi00ODIwLWJhZDgtMzRmNzhlMjdiOGJjIiwiaWF0IjoxNjk5Nzc0MjU3LCJleHAiOjE2OTk3Nzc4NTd9.Q1PX5x7sWJlJbzFVpjHcIySTvxoX0uh7IGtlgI18E94',
    'Cookie': 'lang=en-US'
  }

  # get all incidents from inrix api
  response = requests.request("GET", url, headers=headers, data=payload)
  currentSpeed = json.loads(response.text)["result"]["segmentspeeds"][0]["segments"][0]["speed"]
  return {"currentSegmentSpeed": currentSpeed}
