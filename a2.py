import urllib.request
import urllib.parse
import requests

data = {}
data['name'] = 'Somebody Here'
data['location'] = 'Northampton'
data['language'] = 'Python'
url_values = urllib.parse.urlencode(data)
print(url_values)  # The order may differ from below.

name="Somebody+Here&language=Python&location=Northampton"
url = 'http://www.example.com/example.cgi'
full_url = url + '?' + url_values
data = urllib.request.urlopen(full_url)




r = requests.get("http://example.com/foo/bar")
