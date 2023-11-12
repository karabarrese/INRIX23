import json
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/incidents')
def index():

  point = "37.757386|-122.490667"
  # box = "37.757386|-122.490667,37.746138|-122.395481"
  radius = "100"
  url = f"https://api.iq.inrix.com/v1/incidents?point={point}&radius={radius}&incidentoutputfields=All&incidenttype=Incidents,Construction&locale=en"

  payload = {}
  headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6IjZpeWIwZGYxdGoiLCJ0b2tlbiI6eyJpdiI6IjEwYTY0ODNjYWI1ZGFhNjg4ZDFiOTRmOTRiYWQxNjc2IiwiY29udGVudCI6IjBhMmVlMjgyOWJkN2Y1N2I1M2FjNzcxZTAyNWE2YzJjZWRjNzM3MjIwOWQ2MGQ2YTVhNjI1MjU5OTFmMzUwMDM5ZWZkOTFiYjliN2FjYzIxMzdjZTY5NWM5YjNhYWJhZTE4ZTM3OThjZmIxZWQ1NGRjMzVmYjcxNGU1NGFiNzdlNDcwYWQ5MWIwNmIzMTMzNjc1ZTQzNWNkM2JhMDUzZDAyYzkwODZhNzNmMjFlYThmZmM5NTZhMDI4MzMyMjljMGQxNDdiODM4ZjQxOGFjYTM2YjFkMzMzNjk3OGQ2MTA2OGVjM2FkOWU5YzUxOTgyMDIzOWRmNGZmZmQ5NTg0MWZhMDI4NTU1YzYxYWU0MDMxNmJhNDQ3OGIyOTE4NjZjOTQwNGRjMzE4M2VjZGZiMzVmYTk5ODQ1OWI3OWFlN2Q3Y2U4Njk2ZDU5M2E3ZTZjMWQwZjUzNzQxYjU3ZDM5YTUyNGM3YjMyZTE3ZTNmYTk5ZWEzN2IyMGRlNzlmZGNjMjBjZmVjMTY0NzY0YzJkY2MxOWNjZmRmZGU0N2Y0MGJiOTczMTI0OTU1NWNjMWRkMDNmYTk0ZWUzNWI5NDRmNTJhMjg0MjBlZjgwZjQzZjY0ZmUwZTIyOThlZWE2MjhkZGIxMmE3MjQxYmRjMzMwZWRkOWUxNjk5MmM1NmM0ZmZmMWQwNjc4YzNjZmJhY2JlOTg2NDAzNmQzOTE5MDRlMGFlNWQxYzY0OTM2NzE1ZDgzZmZhODg0ZWJjYjVkMmM2ODgxYjQxNzA0YTA0ODViOTliMmU0NGEyOTBlNDIxNjQ5NmU0ZGYwZjU2NWE2MTQ3MDM1NGNhY2I2NWI0MjA3MGViZWViZjEzY2U3YTFiMDhhY2NlOTM2In0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiIxMGE2NDgzY2FiNWRhYTY4OGQxYjk0Zjk0YmFkMTY3NiIsImNvbnRlbnQiOiIzYjMzZjE5Zjk1ZjVkMTZiNzZiNDY4MjczYjY4NzE1NmMyZTIxYzI1MzZjZDBmM2Q2MTE3NzcwY2FjZmU2OTJmZmM4NmUzZTk4NzY4ODcyMDA1ZDc2YzYyIn0sImp0aSI6IjlmMmM4Y2I2LTVkZDItNGZkZi04NWNiLWU1YWNkMWNjM2ZkMiIsImlhdCI6MTY5OTc1MzM0MCwiZXhwIjoxNjk5NzU2OTQwfQ.SHSJLYw6F3f963VTs9TlDHB4mMrH5AsHWVcjHnhPSyE',
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
