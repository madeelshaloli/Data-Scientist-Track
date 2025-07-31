# Import packages
import requests
from bs4 import BeautifulSoup
# Specify url: url
url='https://www.python.org/~guido/'

# Package the request, send the request and catch the response: r
r=requests.get(url)

# Extracts the response as html: html_doc
html_docs=r.text

# Create a BeautifulSoup object from the HTML: soup

soup=BeautifulSoup(html_docs)
# Prettify the BeautifulSoup object: pretty_soup

pretty_soup=soup.prettify()
# Print the response
print(html_docs)


#exercise 2

# Load JSON: json_data
import json
with open("a_movie.json") as json_file:
    json_data=json.load(json_file)

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])

for k, v in json_data.items():
    print(k + ': ', v)


#exercise 3


# Import requests package

import requests
# Assign URL to variable: url
url='http://www.omdbapi.com/?t=the+social+network&apikey=72bc447a'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Print the text of the response
print(r.text)


#exercise 4


# Import package
import requests

# Assign URL to variable: url
url = 'http://www.omdbapi.com/?apikey=72bc447a&t=social+network'

# Package the request, send the request and catch the response: r
r=requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data=r.json()

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])
print(j)
soup=BeautifulSoup(j, 'html.parser')
print(soup.prettify())



#exercise 5
# Import package
import requests

# Assign URL to variable: url
url='https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data=r.json()

# Print the Wikipedia page extract
pizza_extract = json_data['query']['pages']['24768']['extract']
print(pizza_extract)
