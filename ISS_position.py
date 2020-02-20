from urllib import request
from datetime import datetime
import json

resp = request.urlopen("http://api.open-notify.org/iss-now.json")

obj = json.loads(resp.read())
time = obj['timestamp']
print(datetime.utcfromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S'))
print("ISS Position:\n")

print("Longitude: ", obj['iss_position']['longitude'])
print("Latitude: ", obj['iss_position']['latitude'])


