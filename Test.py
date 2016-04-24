__author__ = 'handwa'

# Client ID: 7e951996e3c2cc7b7d64
# Client Secret: fed16a1234dc41c06ac045e7316d7684cfa8e460

from urllib import parse, request, response
import json

class MyOpener(request.FancyURLopener):
    verison = "test"

map_k = [
    ('client_id','7e951996e3c2cc7b7d64'),('client_secret','fed16a1234dc41c06ac045e7316d7684cfa8e460'),('grant_type','password'),('username','DaNiAnBot'),('password','4bd888ce59c9e74ab4caba6c30452bcf')]
k = parse.urlencode(map_k)
str_k = json.dumps(k)
#k = parse.quote_plus(str_k)
print(k)
values = k.encode('ascii')
#values_temp = "client_id=7e951996e3c2cc7b7d64&client_secret=fed16a1234dc41c06ac045e7316d7684cfa8e460&grant_type=password&username=DaNiAnBot&password=csci4150"
#values = values_temp.encode('ascii')
print(values)
print(type(values))



headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

opener = MyOpener()

request_1 = request.Request('https://online-go.com/oauth2/access_token', data=values, headers=headers)
print(request_1)
response_body = request.urlopen(request_1).read()



print(str(response_body)[2:-1])
formatted = (str(response_body)[2:-1])
formatted = formatted.replace("\\n","")

response_dict = json.loads(formatted)
print(response_dict)

headers['Authorization'] = 'Bearer ' + response_dict["access_token"]

request_2 = request.Request('https://online-go.com/api/v1/me/',headers=headers)
response_body = request.urlopen(request_2).read()
print(response_body)

#values_2='{"player_id":294273}'
values_2='{"player_id":293597}'
headers['Content-Type']="application/json"
request_3=request.Request('https://online-go.com/api/v1/me/friends',data=values_2.encode('ascii'),headers=headers)
response_body = request.urlopen(request_3).read()
print(response_body)





