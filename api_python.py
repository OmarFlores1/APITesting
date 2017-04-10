from urllib.request import urlopen
import json

# Get the dataset. Example taken from http://stackoverflow.com/questions/23049767/parsing-http-response-in-python
url = 'http://www.quandl.com/api/v1/datasets/FRED/GDP.json'
response = urlopen(url)

# Convert bytes to string type and string type to dict
string = response.read().decode('utf-8')
json_obj = json.loads(string)

print("Source: " + json_obj['source_name'])

print("Data type: " + json_obj['name'])

print("Data with values above $18,000:")

for datum in json_obj['data']:
    if datum[1]>18000:
        print(datum)
