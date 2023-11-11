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
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6IjZpeWIwZGYxdGoiLCJ0b2tlbiI6eyJpdiI6IjcxMDU4ZjQ2YjhhZDNiZGJhM2U0NDAxYTU4NjY5MTFjIiwiY29udGVudCI6IjMxOGY1MGMxYTAzNjg5Yjc3ZGRiYWNmZTcyYTBlYzdlMGZkZTc3M2FmMjRlNjMxMGFiM2MwNjQxZGM0MjY3N2RjMDkzZjY1MTFhMTNjMWRkOTdlNTY1ZjRmZGNmNTI0MzY3Zjc1YmUzYmY3OWUxOWNlM2U1NjZkMGZhNWFmYWM0MDliYzMyNTEwNzZjNmMwNzQyNWYzODI0YmM5ZDI2Y2E0ZjNiZDhhNDRmZmZhMWNhMzg0ZjkyZGQ1YTk1YTMwZTY1ZTQwZjQ2YmNhOGVmMzE5NjdiOTkzNjJiYjgwYzhiOGY2OTJhMjI1YWI0Nzc2NTQyMWYyZGEyZGRiNWJkNzAzOGI3ZmM0MTdhZTRiYjIxZjRjMTk2NmExNzlkODU4ODdiZjY3NjlkZjEwN2NmZTRjYWY0ZjVlOWE4ODg1MzcxM2I4OWU1ZmJmYzhiZjUwNTY3YzBjOWEzNDFiOGU1MmRiYTM0NDk5ODFlODA3MjMwZjNlMTFjYmFmZTZjZDM0NjQwOWY5Nzg2NmQwOGM4OTdkYjI2YzAxZTExNzAwNWMwNTkxMmYxNDM3NjEwOTJiMjNlMGIwNzljMDRmYzI0MGViMmJhYWY3ZDQyYmI1NmEwNTU3MWY4ZmZmNWQ5MGQ1YzRhMjVmOTY3NGU4NmM0ODQ4ZDRlMTFjYmU1OWUwNmFjZTcwNzU2YjcxZjM4YTUzNDg1N2Q5MTdhN2MxODBjMjUwYTZmNDFjZGJmY2ZhMDM5MjZjMjk1NjZhMTA5ZWNkZTMxZDVlYTg3NTIyNTNlZWU0MjVmMTRjZjYyNDU4NWQzMGEwODI4ZjAyNTFhMTFjMzI4MTgxZDJjYjE2ZjQxNDY4MDBmZWI1ODkxZDMzNGU2NTk4ZmFlIn0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiI3MTA1OGY0NmI4YWQzYmRiYTNlNDQwMWE1ODY2OTExYyIsImNvbnRlbnQiOiIyMWM0NDhkZjkxM2VhNGVmMDNmYzgwYzM0NWI5ODgwODMxZjM1ZjI4ZWE2YzA0NjNmMTRlMjAzOWYwNmM2ZDQ3ZDBiOWVjNWI2NjFlZDZlNzlkZTExOWNhIn0sImp0aSI6IjQ4ZTczYmM3LTRjOTctNDBlNS1hMmY3LTc3MTg5YzAxYTJkNCIsImlhdCI6MTY5OTczMTIwMCwiZXhwIjoxNjk5NzM0ODAwfQ.B2L4GRkT4yoc_9QZ4-Jhfm99De_Oi_CY2T2VjlE_OBA","expiry":"2023-11-11T20:33:20.244Z',
    'Cookie': 'lang=en-US'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  # print(response.text)
  # return response.text
  # return jsonify(response.text)
  # return jsonify({'name': 'alice2',
  #                 'email': 'alice@outlook.com'})
  # return{"members": ["Member1", "Member2", "Member3"]}
  return{"message":"tiffany will be happy if you show up pls"}

if __name__ == "main":
  app.run(debug=True, host="0.0.0.0", port=5001)