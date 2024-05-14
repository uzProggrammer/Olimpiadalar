import pprint, json
import requests

s=set()
response = requests.get('http://codeforces.com/api/problemset.problems?tags=number%20theory')
for j in json.loads(response.content)['result']['problems']:
    s.add(j['name'])

response2 = requests.get('http://codeforces.com/api/problemset.problems?tags=data%20structures')
for k in json.loads(response2.content)['result']['problems']:
    s.add(k['name'])

response1 = requests.get('http://codeforces.com/api/problemset.problems?tags=implementation')
for i in json.loads(response1.content)['result']['problems']:
    s.add(i['name'])
# pprint.pprint(s)
print(len(s))