# APITesting
simple example of API testing using PostMan and Python

In this example we use the Federal Reserve API with no key http://www.quandl.com/api/v1/datasets/FRED/GDP.json to demonstrate data accessing via API with both PostMan and Python.

We use Python to further manipulate the data:
1. We grab only the desired entry
2. We filter for entries that meet certain criteria (> $18,000).

The result thus parsed gives:

Source: Federal Reserve Economic Data  --  
Data type: Gross Domestic Product  --  
Data with values above $18,000:  --  
['2016-10-01', 18869.4]
['2016-07-01', 18675.3]
['2016-04-01', 18450.1]
['2016-01-01', 18281.6]
['2015-10-01', 18222.8]
['2015-07-01', 18141.9]
