import json
import requests
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def index():

  point = "37.757386|-122.490667"
  # box = "37.757386|-122.490667,37.746138|-122.395481"
  radius = "100"
  url = f"https://api.iq.inrix.com/v1/incidents?point={point}&radius={radius}&incidentoutputfields=All&incidenttype=Incidents,Construction&locale=en"

  payload = {}
  headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6IjZpeWIwZGYxdGoiLCJ0b2tlbiI6eyJpdiI6IjVmNjhiNzhlNGRhNWZhY2JiYmE2NjUxYWZkNzFhZjgzIiwiY29udGVudCI6ImFhNTNmYjBkZjBjMGIwNzI1ZTQ1MTM0MTVkMzE1MzgzZDAzZTM1MzRlNTA1N2Y1N2Q5MGQ0N2YxNGE1NjhmYThlOWJmODQxMmFkM2NkZDQyOTY3MzA2ZWVmMWRjNDZlOWI5NGQ1ZjRhM2QzMjNjODQ1NjZmNWEzNzEzMDlmNGJlNzZmYWI1ZjI1ZjdlY2ZmYjY0YjBjMGNiOTNjNzFlZTk2NDZiYTc5NTJhZjY5MzRjZTIwZDVlM2QwNDFkZDMwNWY5Mzc1NDUzMDAzNDhiNmVmNmIwN2EzOWM3NGY2MDM0NzVlNDIxZDEyYjZmMmNiZDVlMTczZDI5YTVlNGNhYmUyNmFiZmEyMTFlNDFhMjE5MmM5NTg0MzhmZGFkMGQ4ZDk2YzI5MmRhNGM2NzM2YWNjNzJmZGEyMmU1ZWEzMzI2ZjM2MTY3YTI0MDQ1NDVkZjhiYjRmZmU0OWUyNDkzZDVlZTUyNGFhMDYwZGVlMmJlNzM0OWU2ZjE3ODI1Yjc0MGU0MTE4MDY0OWRhZjJlNDZlNmJkMjhkOWU2NjhhZWUyY2FmNjI5M2MxMDRlNmRkZmQ4YTE1NTkwMGExNmI4NTEyNzc4Y2QxZWVhMzYxNTQzY2NjOWM1ODAyODY1NjkxODUzOGJlODI5YWNmOTljMDg1YTQ2MDQ2NTc0ZTNmNTVjNzc4NzRjNjU2NjU4YWU0M2ExNzkyY2VlZjYyODMzODRkZDJiMGEyMWM4MTJjNjI4MmQ4NWI3YTMzM2M3M2Q5YjFiNjljYjNjN2NmOTM1ZjU5NGY5YWUyOTlmMGVjY2ViYTcyZDM0YzAzYzU5ZWRlYTQxM2I3YzY0NjYwYjBkMDdlMDM2ODVhNTgyMjg0MTU5YWU1ZDVhIn0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiI1ZjY4Yjc4ZTRkYTVmYWNiYmJhNjY1MWFmZDcxYWY4MyIsImNvbnRlbnQiOiJhMTc5Y2IzN2U0ZDdhNDRiNDk0OTFkNTI2ZjdhNmFkZmU0MjQzZDAyZmY1YjFkMDVkODBhNDBmZjZkNGNhNWM1ZDM5NmZkNjdjYzNmYzIzOGJjNDM3NmQwIn0sImp0aSI6IjcyNTZlZDk3LTZiMTMtNDBkYi1hMjYwLTYxZjM4MjAwZTk0ZSIsImlhdCI6MTY5OTc0ODU5MCwiZXhwIjoxNjk5NzUyMTkwfQ.RFDuUFhXajvetlG-k-ICTyWTbwI-DpxNGES81exi7jk',
    'Cookie': 'lang=en-US'
  }

  response = requests.request("GET", url, headers=headers, data=payload)
  incidents = json.loads(response.text)["result"]["incidents"]

  my_dict = {"incidents": []}
  my_json = json.dumps(my_dict)
  incidents_json = json.loads(my_json)

  for i in incidents:
    # data_array.append([incidents[0]["geometry"]["coordinates"],i["descriptions"][0]["desc"]])
    newJson = {"location": i["geometry"]["coordinates"],"description": i["descriptions"][0]["desc"]}
    incidents_json["incidents"].append(newJson)
  return incidents_json

if __name__ == "main":
  app.run(debug=True, host="0.0.0.0", port=5001)