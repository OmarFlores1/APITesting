
# Get the dataset. Example taken from http://stackoverflow.com/questions/23049767/parsing-http-response-in-python
# The main objective of this post is to manipulate the data retrieved and get some actionable data.
# Omar Flores, 4/10/2017
# Use python version 3.4.

from urllib.request import urlopen
import json

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
